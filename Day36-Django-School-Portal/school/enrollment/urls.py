from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('schools/', views.school_list, name='schools-list'),
    path('courses/', views.courses_list, name='courses-list'),
    path('schools/<slug:slug>/', views.school_detail, name='school-detail'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('students/', views.students_list, name='students-list'),
    path('student/<slug:slug>/', views.student_detail, name='student_detail')

]
