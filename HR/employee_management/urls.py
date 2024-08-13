from django.urls import path
from .api import EmployeeListAPIView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
]
