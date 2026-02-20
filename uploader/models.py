from django.db import models


class FileUpload(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    drive_file_id = models.CharField(max_length=200, blank=True, null=True)
    drive_file_url = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.employee_id}"

    class Meta:
        ordering = ['-uploaded_at']
