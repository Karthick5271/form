"""
WSGI config for drive_sheets_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drive_sheets_project.settings')

application = get_wsgi_application()
