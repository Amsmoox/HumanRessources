from django.urls import path
from .api import JobPostingListCreateAPIView, ApplicantListCreateAPIView, OnboardingChecklistListCreateAPIView

urlpatterns = [
    path('job-postings/', JobPostingListCreateAPIView.as_view(), name='job-posting-list'),
    path('applicants/', ApplicantListCreateAPIView.as_view(), name='applicant-list'),
    path('onboarding-checklists/', OnboardingChecklistListCreateAPIView.as_view(), name='onboarding-checklist-list'),
]
