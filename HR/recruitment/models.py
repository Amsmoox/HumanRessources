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

class Applicant(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applicants')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='applicants/resumes/')
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Offered', 'Offered'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ])

    def __str__(self):
        return f"{self.name} - {self.job_posting.title}"
