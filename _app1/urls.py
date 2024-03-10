from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentListCreate.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyApiView.as_view(), name='student-detail'),
]
