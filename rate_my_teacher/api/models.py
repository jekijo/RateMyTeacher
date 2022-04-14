from django.db import models

# Create your models here.

class TeacherPage(models.Model):
    name = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=50, default='')
    rating = models.IntegerField(null=False, default=0)


    
class Student(models.Model):
    rating_given = models.IntegerField(null=False, default=0)
    grade_received = models.IntegerField(null=False, default=0)
    subject = models.CharField(max_length=50, default='')
    comment = models.CharField(max_length=500, default='')

