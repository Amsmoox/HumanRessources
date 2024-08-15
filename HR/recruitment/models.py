from django.db import models
from employee_management.models import Employee

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posting_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
