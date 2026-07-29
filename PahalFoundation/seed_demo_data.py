"""
Demo data population script for Pahal Foundation NGO.
Run with: python manage.py shell < seed_demo_data.py
Or:        python seed_demo_data.py (from within the Django shell)
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PahalFoundation.settings')
django.setup()

from django.contrib.auth.models import User, Group
from content.models import Blog, BlogComment, Video, Playlist, Student, Attendance, Volunteer, Progress
from pahal.models import NewVolunteer, ContactUs
from django.utils.text import slugify
import datetime

print("Starting demo data seeding...")

# --- Groups ---
print("\n[1/8] Creating user groups...")
teacher_group, _ = Group.objects.get_or_create(name='teacher')
admin_group,   _ = Group.objects.get_or_create(name='admin')
default_group, _ = Group.objects.get_or_create(name='default')
print("  OK Groups: teacher, admin, default")

# --- Demo Users ---
print("\n[2/8] Creating demo users...")
if not User.objects.filter(username='teacher1').exists():
    t1 = User.objects.create_user(
        username='teacher1', email='teacher1@pahal.com',
        first_name='Priya', last_name='Sharma', password='teacher123'
    )
    t1.groups.add(teacher_group)
    print("  OK teacher1 / teacher123")
else:
    print("  -- teacher1 already exists")

if not User.objects.filter(username='teacher2').exists():
    t2 = User.objects.create_user(
        username='teacher2', email='teacher2@pahal.com',
        first_name='Rahul', last_name='Verma', password='teacher123'
    )
    t2.groups.add(teacher_group)
    print("  OK teacher2 / teacher123")
else:
    print("  -- teacher2 already exists")

# --- Students ---
print("\n[3/8] Creating demo students...")
students_data = [
    (1, 'Aarav Singh',      'Mohan Singh',    '9876543210', 10, 'Male',   'Class 5', 'DPS School'),
    (2, 'Sneha Patel',      'Rajesh Patel',   '9876543211', 9,  'Female', 'Class 4', 'Kendriya Vidyalaya'),
    (3, 'Rohan Kumar',      'Suresh Kumar',   '9876543212', 11, 'Male',   'Class 6', 'Government School'),
    (4, 'Priya Gupta',      'Anil Gupta',     '9876543213', 8,  'Female', 'Class 3', 'St. Mary School'),
    (5, 'Arjun Yadav',      'Ramesh Yadav',   '9876543214', 12, 'Male',   'Class 7', 'Government School'),
    (6, 'Kavya Sharma',     'Deepak Sharma',  '9876543215', 10, 'Female', 'Class 5', 'DPS School'),
    (7, 'Vivaan Mishra',    'Pramod Mishra',  '9876543216', 9,  'Male',   'Class 4', 'Kendriya Vidyalaya'),
    (8, 'Ananya Tiwari',    'Sanjay Tiwari',  '9876543217', 11, 'Female', 'Class 6', 'Government School'),
    (9, 'Aditya Chauhan',   'Vinod Chauhan',  '9876543218', 8,  'Male',   'Class 3', 'Local School'),
    (10,'Ishika Rajput',    'Hemant Rajput',  '9876543219', 13, 'Female', 'Class 8', 'Government School'),
]
for roll, name, parent, phone, age, gender, grade, prev_school in students_data:
    st, created = Student.objects.get_or_create(
        roll_no=roll,
        defaults=dict(
            name=name, parents_name=parent, phone_no=phone,
            age=age, gender=gender, grade=grade, prev_school=prev_school,
            address='Near Pahal Centre, Delhi', active=True
        )
    )
    if created:
        print(f"  OK Student #{roll}: {name}")
    else:
        print(f"  -- Student #{roll} already exists")

# --- Attendance ---
# Note: Attendance.date has auto_now_add=True — we can only create today's attendance.
print("\n[4/8] Creating attendance records for today...")
import random
statuses = ['Present', 'Absent', 'Present', 'Present', 'Present']
created_count = 0
for roll, name, *_ in students_data:
    st = Student.objects.get(roll_no=roll)
    today = datetime.date.today()
    if not Attendance.objects.filter(student=st, date=today).exists():
        try:
            att = Attendance(student=st, status=random.choice(statuses))
            att.save()
            created_count += 1
        except Exception as e:
            print(f"  WARN: Could not create attendance for {name}: {e}")
print(f"  OK Created attendance for {created_count} students (today's date)")

# --- Progress Records ---
print("\n[5/8] Creating student progress records...")
grades = ['Excellent', 'Good', 'Satisfactory', 'Needs Improvement']
for roll, name, *_ in students_data:
    st = Student.objects.get(roll_no=roll)
    if not st.progress_repost.exists():
        Progress.objects.create(
            student=st,
            math=random.choice(grades),
            hindi=random.choice(grades),
            english=random.choice(grades),
            extra_curricular=random.choice(grades),
        )
        print(f"  OK Progress for {name}")

# --- Volunteers ---
print("\n[6/8] Creating demo volunteers...")
volunteers_data = [
    ('PF-2024-001', 'Dr. Meera Joshi',    'Program Director',  'meera@pahal.com',   '9811234567', 'Education, Child Welfare',    '5 years NGO work'),
    ('PF-2024-002', 'Amit Khanna',        'Math Teacher',      'amit@pahal.com',    '9811234568', 'Mathematics, Science',        '3 years teaching'),
    ('PF-2024-003', 'Sunita Rawat',       'Hindi Teacher',     'sunita@pahal.com',  '9811234569', 'Hindi Literature',            '4 years teaching'),
    ('PF-2024-004', 'Vikram Bose',        'Sports Coach',      'vikram@pahal.com',  '9811234570', 'Sports, Fitness',             '6 years coaching'),
    ('PF-2024-005', 'Riya Nair',          'Art Teacher',       'riya@pahal.com',    '9811234571', 'Art & Craft, Music',          '2 years teaching'),
    ('PF-2024-006', 'Suresh Rao',         'English Teacher',   'suresh@pahal.com',  '9811234572', 'English, Communication',      '5 years teaching'),
]
for reg, name, desig, email, phone, interest, exp in volunteers_data:
    vol, created = Volunteer.objects.get_or_create(
        Reg_no=reg,
        defaults=dict(name=name, designation=desig, email=email,
                      phone_no=phone, interest=interest, experience=exp)
    )
    if created:
        print(f"  OK Volunteer: {name} ({desig})")
    else:
        print(f"  -- {name} already exists")

# --- Blog Posts ---
print("\n[7/8] Creating demo blog posts...")
admin_user = User.objects.filter(is_superuser=True).first()
blogs_data = [
    (
        "Pahal Foundation: Transforming Lives Through Education",
        "pahal-foundation-transforming-lives",
        "<p>Education is the most powerful weapon which you can use to change the world. At Pahal Foundation, we believe every child, regardless of their background, deserves quality education and a brighter future.</p><p>Since our inception, we have been working tirelessly to bridge the education gap in underprivileged communities across Delhi. Our dedicated team of volunteers brings passion, expertise, and love to every classroom session.</p><p>This year alone, we have enrolled over 50 new students and expanded our curriculum to include digital literacy, spoken English, and creative arts.</p>"
    ),
    (
        "Annual Sports Day 2024: Building Team Spirit",
        "annual-sports-day-2024",
        "<p>Last Saturday was a day full of energy, laughter, and incredible sportsmanship at Pahal Foundation's Annual Sports Day 2024! Over 60 students participated in various events including running races, tug of war, and sack races.</p><p>Sports play a crucial role in a child's holistic development. They learn teamwork, discipline, and how to handle both victory and defeat gracefully.</p>"
    ),
    (
        "Digital Literacy: Preparing Students for Tomorrow",
        "digital-literacy-preparing-students",
        "<p>In today's rapidly evolving digital world, computer literacy is no longer a luxury - it is a necessity. Recognizing this, Pahal Foundation has launched a dedicated Digital Literacy Program for our students.</p><p>Thanks to generous donations, we have set up a small computer lab with 8 systems. Students are learning basic computer operations, MS Office, and internet safety.</p>"
    ),
    (
        "Parent-Teacher Meeting: Strengthening the Bond",
        "parent-teacher-meeting-2024",
        "<p>A successful Parent-Teacher Meeting was held at our centre last weekend. Over 40 parents attended, making it our most well-attended PTM to date! Parents got to meet their children's teachers, review progress reports, and discuss areas for improvement.</p>"
    ),
    (
        "Volunteer Spotlight: Meet Dr. Meera Joshi",
        "volunteer-spotlight-meera-joshi",
        "<p>Every month, we shine a light on one of our incredible volunteers. This month, we celebrate Dr. Meera Joshi, our Program Director who has been with Pahal Foundation for over 5 years.</p><p>Dr. Meera holds a PhD in Education Policy and has dedicated her post-retirement years entirely to child welfare. Her leadership and vision have shaped Pahal's curriculum and teaching methodology.</p>"
    ),
]
for title, slug, content_html in blogs_data:
    if not Blog.objects.filter(slug=slug).exists():
        Blog.objects.create(
            owner=admin_user, title=title, slug=slug,
            content=content_html, views=random.randint(50, 500), likes=random.randint(10, 100)
        )
        print(f"  OK Blog: {title[:55]}...")
    else:
        print(f"  -- Blog '{slug}' already exists")

# --- Playlists & Videos ---
print("\n[8/8] Creating demo playlists and videos...")
pl1, created = Playlist.objects.get_or_create(
    slug='PL001',
    defaults=dict(pf='1', title='Basic Mathematics for Class 4-6', visible=True,
                  desc='A comprehensive playlist covering arithmetic, fractions, and basic geometry for Pahal students.')
)
if created: print("  OK Playlist: Basic Mathematics")

pl2, created = Playlist.objects.get_or_create(
    slug='PL002',
    defaults=dict(pf='1', title='Spoken English Basics', visible=True,
                  desc='Fun and interactive videos to help students learn spoken English with confidence.')
)
if created: print("  OK Playlist: Spoken English Basics")

videos_data = [
    ('PL001xxx-1', '1', 'Addition and Subtraction Made Easy',    True, 'Learn the basics of addition and subtraction with fun examples!',     'https://www.youtube.com/embed/dQw4w9WgXcQ', 120, 45),
    ('PL001xxx-2', '1', 'Understanding Fractions',               True, 'What is a fraction? Learn with pizzas and fun visuals!',              'https://www.youtube.com/embed/dQw4w9WgXcQ', 98,  38),
    ('PL001xxx-3', '1', 'Multiplication Tables 1-10',            True, 'Master all multiplication tables with easy tricks and songs.',         'https://www.youtube.com/embed/dQw4w9WgXcQ', 210, 67),
    ('PL001xxx-4', '1', 'Introduction to Geometry',              True, 'Shapes, angles, and basic geometry concepts explained simply.',        'https://www.youtube.com/embed/dQw4w9WgXcQ', 88,  30),
    ('PL002xxx-1', '1', 'How to Introduce Yourself in English',  True, 'Learn to confidently introduce yourself in English.',                  'https://www.youtube.com/embed/dQw4w9WgXcQ', 300, 92),
    ('PL002xxx-2', '1', 'Common English Phrases for Daily Use',  True, '50 everyday English phrases every student should know.',              'https://www.youtube.com/embed/dQw4w9WgXcQ', 175, 58),
    ('PL002xxx-3', '1', 'English Alphabet and Phonics',          True, 'Fun phonics lessons to improve pronunciation and reading.',           'https://www.youtube.com/embed/dQw4w9WgXcQ', 140, 48),
    ('SAxxx00001', '0', 'Pahal Foundation - Our Story',          True, 'Watch how Pahal Foundation started and the impact we have made.',     'https://www.youtube.com/embed/dQw4w9WgXcQ', 450, 120),
    ('SAxxx00002', '0', 'Student Success Stories 2024',          True, 'Inspiring stories of students who transformed their lives at Pahal.', 'https://www.youtube.com/embed/dQw4w9WgXcQ', 320, 88),
    ('SAxxx00003', '0', 'How to Support Pahal Foundation',       True, 'Learn about different ways you can contribute and make a difference.','https://www.youtube.com/embed/dQw4w9WgXcQ', 230, 72),
]
for slug, pf, title, visible, desc, source, views, likes in videos_data:
    v, created = Video.objects.get_or_create(
        slug=slug,
        defaults=dict(pf=pf, title=title, visible=visible, desc=desc,
                      source=source, views=views, likes=likes)
    )
    if created:
        print(f"  OK Video: {title[:50]}")
    else:
        print(f"  -- Video '{slug}' already exists")

# --- Contact Us Submissions ---
print("\n[+] Creating sample Contact Us submissions...")
contacts_data = [
    ('Neha Agarwal',  'neha@example.com',   '9812345678', 'Donation Query',          'I would like to know how I can donate monthly to support your students.'),
    ('Rakesh Sharma', 'rakesh@example.com', '9812345679', 'Volunteering Interest',   'I am a retired teacher and would love to volunteer at your centre on weekends.'),
    ('Pooja Singh',   'pooja@example.com',  '9812345680', 'Admission for my child',  'My daughter is 9 years old. I would like to enrol her in your program. Please guide me.'),
]
for name, email, phone, subject, message in contacts_data:
    ContactUs.objects.get_or_create(email=email,
        defaults=dict(fullName=name, phoneNo=phone, subject=subject, message=message))
print(f"  OK {len(contacts_data)} contact submissions added")

# --- New Volunteer Applications ---
print("\n[+] Creating sample volunteer applications...")
new_vols_data = [
    ('Ankit Dubey',   'ankit@example.com',   '9823456789', 'Science & Technology', 'I am a software engineer. I want to teach coding basics.'),
    ('Shalini Mehta', 'shalini@example.com', '9823456790', 'Arts & Crafts',        'I am an artist and would love to run weekly art sessions for the children.'),
    ('Manoj Tiwari',  'manoj@example.com',   '9823456791', 'Sports & Fitness',     'I am a certified fitness trainer, happy to help with sports and physical education.'),
]
for name, email, phone, interest, about in new_vols_data:
    NewVolunteer.objects.get_or_create(email=email,
        defaults=dict(fullName=name, phoneNo=phone, interestArea=interest, about=about))
print(f"  OK {len(new_vols_data)} volunteer applications added")

print("\n" + "="*55)
print("DEMO DATA SEEDING COMPLETE!")
print("="*55)
print(f"  Students:               {Student.objects.count()}")
print(f"  Attendance records:     {Attendance.objects.count()}")
print(f"  Progress records:       {Progress.objects.count()}")
print(f"  Volunteers:             {Volunteer.objects.count()}")
print(f"  Blog posts:             {Blog.objects.count()}")
print(f"  Videos:                 {Video.objects.count()}")
print(f"  Playlists:              {Playlist.objects.count()}")
print(f"  Contact submissions:    {ContactUs.objects.count()}")
print(f"  Volunteer applications: {NewVolunteer.objects.count()}")
print(f"  Users:                  {User.objects.count()}")
print("\nAdmin:   http://127.0.0.1:8000/admin/")
print("Website: http://127.0.0.1:8000/")

