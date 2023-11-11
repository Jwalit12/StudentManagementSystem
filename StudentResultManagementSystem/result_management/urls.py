# result_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('add_result/', views.add_result, name='add_result'),
    path('result_list/', views.result_list, name='result_list'),
]
