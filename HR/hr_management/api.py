from rest_framework import generics
from .models import Skill, EmployeeSkill, PerformanceReview, LearningProgram, Bonus
from .serializers import SkillSerializer, EmployeeSkillSerializer, PerformanceReviewSerializer, LearningProgramSerializer, BonusSerializer

class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeeSkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer

class PerformanceReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

class LearningProgramListCreateAPIView(generics.ListCreateAPIView):
    queryset = LearningProgram.objects.all()
    serializer_class = LearningProgramSerializer

class BonusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer
