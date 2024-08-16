from rest_framework import generics
from .models import JobPosting, Applicant
from .serializers import JobPostingSerializer, ApplicantSerializer


class JobPostingListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ApplicantListCreateAPIView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
