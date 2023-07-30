from django.shortcuts import render,redirect
from .models import *
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password 

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Student.objects.filter(email=email).exists():
            return HttpResponse("Email exists,please enter an other email")
        else:
            Student.objects.create(name=name , email=email , password=password)
            return redirect('/')

def login(request):
     if request.method == 'POST':
         email = request.POST['email']
         user_pass = request.POST['password']
         if Student.objects.filter(email=email).exists():
             obj = Student.objects.get(email=email)
             password = obj.password
             if check_password(user_pass,password):
                 return redirect("/dashboard/")
             else:
                 return HttpResponse("please enter correct password")
         else:
             return HttpResponse("Email not found,please sign-up first")

def dashboard(request):
    return render(request,'dashboard.html')

def courses(request):
    return render(request,'courses.html')

def addCourse(request):
    if request.method == 'POST':
        course = request.POST['course']
        fees = request.POST['fees']
        duration = request.POST['duration']
        comment = request.POST['comment']
        AddCourses.objects.create(course=course , fees=fees, duration=duration, comment=comment)
        return render(request,'courses.html')

def signup(request):
    return render(request,'sign-up.html')

def tables(request):
    return render(request,'tables.html')

def viewstudent(request):
    return render(request,'viewstudent.html')