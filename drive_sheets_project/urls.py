"""
URL configuration for drive_sheets_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uploader.urls')),
]
