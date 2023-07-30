from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('signup/',views.signup),
    path('courses/',views.courses),
    path('viewstudent/',views.viewstudent),
    path('tables/',views.tables),
    path('registration/',views.registration),
    path('login/',views.login),
    path('course/',views.addCourse),
]
