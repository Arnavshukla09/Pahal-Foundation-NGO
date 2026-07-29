from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Blog, Student, Attendance, Volunteer, Progress
from .forms import WriteBlog, Admission, VolunteerEnrolment
from .decorators import allowed_users
import datetime

def get_dashboard_stats():
    """Return common stats used across all dashboard pages."""
    today = timezone.now().date()
    total_students = Student.objects.filter(active=True).count()
    total_volunteers = Volunteer.objects.count()
    total_blogs = Blog.objects.count()

    today_att = Attendance.objects.filter(date=today)
    today_present = today_att.filter(status__iexact='present').count()
    today_pct = round((today_present / total_students * 100) if total_students else 0)

    # Weekly attendance (last 7 days)
    week_start = today - datetime.timedelta(days=6)
    week_att = Attendance.objects.filter(date__gte=week_start)
    week_present = week_att.filter(status__iexact='present').count()
    week_total = week_att.count()
    week_pct = round((week_present / week_total * 100) if week_total else 0)

    return {
        'total_students': total_students,
        'total_volunteers': total_volunteers,
        'total_blogs': total_blogs,
        'today_attendance': today_pct,
        'weekly_attendance': week_pct,
    }

# Create your views here.
@login_required(login_url='/login/')
def profile(request):
    stats = get_dashboard_stats()
    # Recent students
    recent_students = Student.objects.filter(active=True).order_by('-date')[:5]
    # Today's attendance detail
    today = timezone.now().date()
    today_records = Attendance.objects.filter(date=today).select_related('student')
    context = {**stats, 'recent_students': recent_students, 'today_records': today_records}
    return render(request, 'content/profile.html', context)

@login_required(login_url='/login/')
def timetable(request):
    return render(request, 'content/timetable.html', get_dashboard_stats())

@allowed_users(allowed_roles=['admin'])
def create_blog(request):
    form = WriteBlog()
    if request.method == 'POST':
        form = WriteBlog(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.slug = slugify(blog.title)
            blog.views = blog.likes = 0
            blog.save()
            return redirect('/dashboard/my_blogs/')
        else:
            messages.error(request, "Form is showing invalid.")
    context = {**get_dashboard_stats(), 'form': form}
    return render(request, 'content/blogcreate.html', context)

@allowed_users(allowed_roles=['admin'])
def my_blogs(request):
    blogs = Blog.objects.filter(owner=request.user).order_by('-time')
    context = {**get_dashboard_stats(), 'blogs': blogs}
    return render(request, 'content/my_blogs.html', context)

@allowed_users(allowed_roles=['teacher', 'admin'])
def student_info(request):
    students = Student.objects.filter().order_by('roll_no')
    context = {**get_dashboard_stats(), 'students': students}
    return render(request, 'content/students_info.html', context)

@allowed_users(allowed_roles=['teacher','admin'])
def attendance(request):
    students = Student.objects.filter(active=1).order_by('roll_no')

    if request.method == "POST":
        try:
            with transaction.atomic():
                for st in students:
                    status = request.POST.get("rollNo" + str(st.roll_no))
                    att = Attendance(student=st, status=status)
                    att.save()
            return redirect("/dashboard/profile")
        except Exception as e:
            messages.error(request, "Unable to save attendance: " + str(e))

    context = {**get_dashboard_stats(), 'students': students}
    return render(request, 'content/attendance.html', context)

@allowed_users(allowed_roles=['teacher', 'admin'])
def admission(request):
    if request.method == 'POST':
        form = Admission(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/student-info/')
        else:
            messages.error(request, "Admission form is showing invalid.")
    context = {**get_dashboard_stats()}
    return render(request, 'content/admission.html', context)

@allowed_users(allowed_roles=['admin'])
def volunteer_info(request):
    volunteer = Volunteer.objects.all()
    context = {**get_dashboard_stats(), 'volunteer': volunteer}
    return render(request, 'content/volunteer_info.html', context)
@allowed_users(allowed_roles=['admin'])
def volunteer_enrolment(request):
    if request.method == 'POST':
        form = VolunteerEnrolment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/volunteer-info')
        else:
            messages.error(request, "Volunteer enrolment form is showing invalid.")
    return render(request, 'content/volunteer_enrolment.html')
