from django.contrib import admin
from .models import FileUpload

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'phone', 'uploaded_at')
    search_fields = ('name', 'employee_id', 'phone')
    list_filter = ('uploaded_at',)
