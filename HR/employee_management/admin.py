from django.contrib import admin
from .models import Employee, PersonalInformation, EmergencyContact, BankInfo, FamilyInfo, EducationInfo, Experience

admin.site.register(Employee)
admin.site.register(PersonalInformation)
admin.site.register(EmergencyContact)
admin.site.register(BankInfo)
admin.site.register(FamilyInfo)
admin.site.register(EducationInfo)
admin.site.register(Experience)
