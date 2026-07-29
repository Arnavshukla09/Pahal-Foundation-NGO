"""
WSGI config for PahalFoundation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Fix for Vercel: add the PahalFoundation project dir to sys.path
# Vercel runs from /var/task/ (repo root), so Python can't find
# 'PahalFoundation.settings' unless we add /var/task/PahalFoundation/ to the path.
# __file__ = /var/task/PahalFoundation/PahalFoundation/wsgi.py
# .parent.parent = /var/task/PahalFoundation/  <-- this is what we need
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PahalFoundation.settings')

application = get_wsgi_application()

# Vercel requires the WSGI callable to be named `app`
app = application
