from django.shortcuts import render
from rest_framework import generics
from .serializers import TeacherSerializer
from .models import TeacherPage

# Create your views here.

class TeacherPageView(generics.CreateAPIView):
    queryset = TeacherPage.objects.all()
    serializer_class = TeacherSerializer
