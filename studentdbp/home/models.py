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

class AddStudents(models.Model):
    sname = models.CharField(max_length=100,blank=True, null=True)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    stotalAmount = models.IntegerField()
    spaidAmount = models.IntegerField()
    sdueAmount = models.IntegerField()
    scourse = models.ForeignKey(AddCourses, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class AddTeachers(models.Model):
    tname = models.CharField(max_length=250)
    temp_id = models.CharField(max_length=250)
    temail = models.EmailField(max_length=250)
    tpsw = models.CharField(max_length=255)
    tmobile = models.IntegerField()
    tjoindate = models.CharField(max_length=250)
    teducation = models.CharField(max_length=250)
    tgender = models.CharField(max_length=250)
    tcourse = models.ForeignKey(AddCourses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tname
    
    