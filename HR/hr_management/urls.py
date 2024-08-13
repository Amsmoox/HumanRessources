from django.urls import path
from .api import SkillListCreateAPIView, EmployeeSkillListCreateAPIView, PerformanceReviewListCreateAPIView, LearningProgramListCreateAPIView, BonusListCreateAPIView

urlpatterns = [
    path('skills/', SkillListCreateAPIView.as_view(), name='skill-list'),
    path('employee-skills/', EmployeeSkillListCreateAPIView.as_view(), name='employee-skill-list'),
    path('performance-reviews/', PerformanceReviewListCreateAPIView.as_view(), name='performance-review-list'),
    path('learning-programs/', LearningProgramListCreateAPIView.as_view(), name='learning-program-list'),
    path('bonuses/', BonusListCreateAPIView.as_view(), name='bonus-list'),
]
