from rest_framework import serializers
from .models import Skill, EmployeeSkill, PerformanceReview, LearningProgram, Bonus

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EmployeeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSkill
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'

class LearningProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProgram
        fields = '__all__'

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'
