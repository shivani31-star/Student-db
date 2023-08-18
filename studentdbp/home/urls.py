from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('signup/',views.signup),
    path('courses/',views.courses),
    path('viewstudent/',views.viewstudent,name="viewstudent"),
    path('tables/',views.tables),
    path('registration/',views.registration),
    path('login/',views.login),
    path('course/',views.addCourse),
    path('updatec/<int:uid>',views.update_v_course),
    path('updatec/',views.update_course),
    path('delete/<int:pk>',views.delete_course,name="delete"),
    path('addstudent/',views.addStudent),
    path('deletestu/<int:pk>',views.delete_st,name="deletestu"),
    path('updatest/<int:sid>',views.update_stu_view),
    path('updatest/',views.update_stu),
    path('search/',views.search_st, name="search"),
    path('searchc/',views.search_c,name="searchc"),
    path('teachers/',views.teachers),
    path('addteachers/',views.addTeachers),
    path('searcht/',views.search_t,name="searcht"),
    path('deletet/<int:pk>',views.delete_t,name="deletet")
]
