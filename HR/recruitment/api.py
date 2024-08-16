from rest_framework import generics
from .models import JobPosting, Applicant, OnboardingChecklist
from .serializers import JobPostingSerializer, ApplicantSerializer, OnboardingChecklistSerializer

class JobPostingListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ApplicantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class OnboardingChecklistListCreateAPIView(generics.ListCreateAPIView):
    queryset = OnboardingChecklist.objects.all()
    serializer_class = OnboardingChecklistSerializer 
