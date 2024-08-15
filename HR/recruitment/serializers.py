from rest_framework import serializers
from .models import JobPosting, Applicant, OnboardingChecklist

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class OnboardingChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnboardingChecklist
        fields = '__all__'
