#!/usr/bin/env bash
# build.sh — Render.com build script
# This runs once every time you deploy

set -o errexit   # Exit on any error

# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Collect all static files into /staticfiles
python manage.py collectstatic --no-input

# 3. Apply database migrations
python manage.py migrate

# 4. Seed demo data (idempotent — safe to run multiple times)
python -c "
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PahalFoundation.settings')
django.setup()
from django.contrib.auth.models import User, Group

# Create groups
for g in ['admin', 'teacher', 'default']:
    Group.objects.get_or_create(name=g)

# Create admin superuser
if not User.objects.filter(username='aarrn').exists():
    User.objects.create_superuser('aarrn', 'admin@pahal.com', 'admin1234')
    print('Created admin: aarrn / admin1234')

# Create demo teacher
teacher_group = Group.objects.get(name='teacher')
if not User.objects.filter(username='teacher_demo').exists():
    t = User.objects.create_user('teacher_demo', 'teacher@pahal.com', 'teacher123',
                                  first_name='Anjali', last_name='Mehta')
    t.groups.add(teacher_group)
    print('Created teacher: teacher_demo / teacher123')
"
echo "Build complete."
