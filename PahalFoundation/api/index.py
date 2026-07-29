import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PahalFoundation.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel expects the WSGI app to be named `app`
app = application
