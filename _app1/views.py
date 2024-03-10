# from django.shortcuts import render
# from rest_framework import generics
# from .models import Students
# from .serializers import StudentSerializers

# class StudentListCreateApiView(generics.ListCreateAPIView):
#     queryset=Students.objects.all()
#     serializer_class=StudentSerializers

# class StudentRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
#     queryset=Students.objects.all()
#     serializer_class=StudentSerializers


from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializers import StudentSerializers  # Corrected import

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers  # Corrected serializer class name

class StudentRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers  # Corrected serializer class name
