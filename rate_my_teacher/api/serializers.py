from rest_framework import serializers
from .models import TeacherPage

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPage
        fields = ('id', 'name', 'school', 'subject', 'rating')