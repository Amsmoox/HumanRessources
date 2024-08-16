from rest_framework import generics
from .models import JobPosting
from .serializers import JobPostingSerializer

class JobPostingListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer