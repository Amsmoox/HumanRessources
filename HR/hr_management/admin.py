from django.contrib import admin

# Register your models here.
from .models import Skill, EmployeeSkill, PerformanceReview, LearningProgram, Bonus

admin.site.register(Skill)
admin.site.register(EmployeeSkill)
admin.site.register(PerformanceReview)
admin.site.register(LearningProgram)
admin.site.register(Bonus)