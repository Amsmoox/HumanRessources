from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='employees/photos/', null=True, blank=True)
    role = models.CharField(max_length=255)
    additional_roles = models.CharField(max_length=255, null=True, blank=True)
    employee_id = models.CharField(max_length=100, unique=True)
    date_join = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    additional_email = models.EmailField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='supervisees')

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class PersonalInformation(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    passport_id_number = models.CharField(max_length=100)
    passport_expiration = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=100)
    spouse_employment = models.CharField(max_length=255, null=True, blank=True)
    children_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Personal Information for {self.employee.name}"

class EmergencyContact(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Emergency Contact: {self.name} ({self.relationship}) for {self.employee.name}"

class BankInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    bank_acc_no = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=11)
    pan_no = models.CharField(max_length=10)

    def __str__(self):
        return f"Bank Info for {self.employee.name}"

class FamilyInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Family Info: {self.name} ({self.relationship}) for {self.employee.name}"

class EducationInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=255)
    start_date = models.DateField()
    finish_date = models.DateField()
    diploma = models.CharField(max_length=255)

    def __str__(self):
        return f"Education: {self.university_name} for {self.employee.name}"

class Experience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Experience: {self.company_name} ({self.role}) for {self.employee.name}"
