from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def allowed_users(allowed_roles=[]):
    """
    Restrict a view to users whose primary group is in allowed_roles.
    Superusers (admin account) bypass the check and always have access.
    """
    def decorator(view_func):
        @login_required(login_url="/login/")
        def wrapper_func(request, *args, **kwargs):
            # Superusers always have full access
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # Return a proper dashboard-styled access denied page
                from django.shortcuts import render
                return render(request, 'content/access_denied.html', {
                    'required_roles': allowed_roles,
                    'user_role': group or 'none',
                }, status=403)
        return wrapper_func
    return decorator
