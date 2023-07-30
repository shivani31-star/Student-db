from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=255)

class AddCourses(models.Model):
    course = models.CharField(max_length=250)
    fees = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    comment = models.TextField()