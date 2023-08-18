from django.shortcuts import render, redirect
from .models import *
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "index.html")


def registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if Student.objects.filter(email=email).exists():
            return HttpResponse("Email exists,please enter an other email")
        else:
            Student.objects.create(name=name, email=email, password=password)
            return redirect("/")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_pass = request.POST["password"]
        if Student.objects.filter(email=email).exists():
            obj = Student.objects.get(email=email)
            password = obj.password
            if check_password(user_pass, password):
                return redirect("/dashboard/")
            else:
                return HttpResponse("please enter correct password")
        else:
            return HttpResponse("Email not found,please sign-up first")


def dashboard(request):
    return render(request, "dashboard.html")


def courses(request):
    course_obj = AddCourses.objects.all()
    return render(request, "courses.html", {"course_obj": course_obj})


def addCourse(request):
    if request.method == "POST":
        course = request.POST["course"]
        fees = request.POST["fees"]
        duration = request.POST["duration"]
        comment = request.POST["comment"]
        AddCourses.objects.create(
            course=course, fees=fees, duration=duration, comment=comment
        )
        return redirect("/courses/")


def update_v_course(request, uid):
    res = AddCourses.objects.get(id=uid)
    return render(request, "update.html", {"data": res})


def update_course(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        course = request.POST["course"]
        fees = request.POST["fees"]
        duration = request.POST["duration"]
        comment = request.POST["comment"]
        AddCourses.objects.filter(id=uid).update(
            course=course, fees=fees, duration=duration, comment=comment
        )
        return redirect("/courses/")


def delete_course(request, pk):
    AddCourses.objects.filter(id=pk).delete()
    return redirect("/courses/")


def signup(request):
    return render(request, "sign-up.html")


def tables(request):
    return render(request, "tables.html")


def viewstudent(request):
    data_stu = AddStudents.objects.all()
    data_course = AddCourses.objects.all()
    redirect("/viewstudent/")
    return render(
        request, "viewstudent.html", {"data_stu": data_stu, "data_course": data_course}
    )


def addStudent(request):
    if request.method == "POST":
        sname = request.POST.get("name")
        semail = request.POST.get("email")
        smobile = request.POST.get("mobile")
        sdegree = request.POST.get("degree")
        scollege = request.POST.get("college")
        scourse_id = request.POST.get("course")
        stotalAmount = request.POST.get("totalAmount")
        spaidAmount = request.POST.get("paidAmount")
        sdueAmount = request.POST.get("dueAmount")
        stu_course = AddCourses.objects.get(id=scourse_id)
        if AddStudents.objects.filter(semail=semail).exists():
            messages.error(request, "email already exists")
            return redirect("/viewstudent/")
        elif AddStudents.objects.filter(smobile=smobile).exists():
            messages.error(request, "Mobile number already exists")
            return redirect("/viewstudent/")
        else:
            AddStudents.objects.create(
                sname=sname,
                semail=semail,
                smobile=smobile,
                scollege=scollege,
                sdegree=sdegree,
                scourse=stu_course,
                stotalAmount=stotalAmount,
                spaidAmount=spaidAmount,
                sdueAmount=sdueAmount,
            )
            messages.success(request, "student added successfully")
            data_stu = AddStudents.objects.all()
            data_course = AddCourses.objects.all()
            return render(
                request,
                "viewstudent.html",
                {"data_stu": data_stu, "data_course": data_course},
            )
    else:
        data_stu = AddStudents.objects.all()
        data_course = AddCourses.objects.all()
        return render(
            request,
            "viewstudent.html",
            {"data_stu": data_stu, "data_course": data_course},
        )

def delete_st(request, pk):
    AddStudents.objects.filter(id=pk).delete()
    return redirect("/addstudent/")


def update_stu_view(request, sid):
    res = AddStudents.objects.get(id=sid)
    data_course = AddCourses.objects.all()
    return render(
        request, "update_stu.html", {"data_s": res, "data_course": data_course}
    )


def update_stu(request):
    if request.method == "POST":
        sid = request.POST["sid"]
        sname = request.POST["name"]
        semail = request.POST["email"]
        smobile = request.POST["mobile"]
        sdegree = request.POST["degree"]
        scollege = request.POST["college"]
        scourse_id = request.POST["course"]
        stotalAmount = request.POST["totalAmount"]
        spaidAmount = request.POST["paidAmount"]
        sdueAmount = request.POST["dueAmount"]
        AddStudents.objects.filter(id=sid).update(
            sname=sname,
            semail=semail,
            smobile=smobile,
            scollege=scollege,
            sdegree=sdegree,
            stotalAmount=stotalAmount,
            spaidAmount=spaidAmount,
            sdueAmount=sdueAmount,
        )
        return redirect("/addstudent/")


def search_st(request):
    if "q" in request.GET:
        q = request.GET["q"]
        multiple_q = (
            Q(Q(sname__icontains=q))
            | Q(Q(semail__icontains=q))
            | Q(Q(smobile__icontains=q))
        )

        data_stu = AddStudents.objects.filter(multiple_q)
    else:
        data_stu = AddStudents.objects.all()
    context = {"data_stu": data_stu}
    return render(request, "viewstudent.html", context)

def search_c(request):
    if "q" in request.GET:
        q = request.GET["q"]
        multiple_q = (Q(Q(course__icontains=q))) | Q(Q(fees__icontains=q))
        course_obj = AddCourses.objects.filter(multiple_q)
    else:
        course_obj = AddCourses.objects.all()
    context = {"course_obj" : course_obj}
    return render(request,"courses.html", context)

def teachers(request):
    data_t = AddTeachers.objects.all()
    data_course = AddCourses.objects.all()
    return render(request,'teacher.html',{"data_t": data_t, "data_course" : data_course})

def addTeachers(request):
    if request.method == 'POST':
        tname = request.POST.get("name")
        temp_id = request.POST.get("emp_id")
        temail = request.POST.get("email")
        tpsw = request.POST.get("psw")
        tmobile = request.POST.get("mobile")
        tjoindate = request.POST.get("joindate")
        teducation = request.POST.get("education")
        tgender = request.POST.get("gender")
        tcourse_id = request.POST.get("course")
        t_course = AddCourses.objects.get(id=tcourse_id)
        if AddTeachers.objects.filter(temail=temail).exists():
            messages.error(request, "email already exists")
            return redirect("/teachers/")
        elif AddTeachers.objects.filter(tmobile=tmobile).exists():
            messages.error(request,"Mobile already exists")
            return redirect("/teachers/")
        else:
            AddTeachers.objects.create(
                tname = tname,
                temp_id = temp_id,
                temail = temail,
                tpsw = tpsw,
                tmobile = tmobile,
                tjoindate = tjoindate,
                teducation = teducation,
                tgender = tgender,
                tcourse = t_course,
            )
            messages.success(request,"successful")
            data_t = AddTeachers.objects.all()
            data_course = AddCourses.objects.all()
            return render(request,'teacher.html',{"data_t" : data_t , "data_course" : data_course})
        
def search_t(request):
    if "q" in request.GET:
        q = request.GET["q"]
        multiple_q = Q(Q(tname__icontains=q)) | Q(Q(temail__icontains=q)) | Q(Q(tmobile__icontains=q))
        data_t = AddTeachers.objects.filter(multiple_q)
    else:
        data_t = AddTeachers.objects.all()
    context = {"data_t" : data_t}
    return render(request,"teacher.html", context)
        
def delete_t(request,pk):
    AddTeachers.objects.filter(id=pk).delete()
    return redirect("/teachers/")