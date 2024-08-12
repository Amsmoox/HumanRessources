from django.db import models

# Create your models here.
from employee_management.models import Employee

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced
    acquired_date = models.DateField()

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    reviewer = models.CharField(max_length=255)
    comments = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # Rating out of 5.00

class LearningProgram(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee)

class Bonus(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_awarded = models.DateField()
    reason = models.TextField(null=True, blank=True)