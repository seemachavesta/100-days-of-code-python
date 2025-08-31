from django.shortcuts import render, get_object_or_404
from .models import School, Course, Student



def dashboard(request):
    context = {
        'school_count': School.objects.count(),
        'courses_count': Course.objects.count(),
        'student_count': Student.objects.count(),
        'recent_courses': Student.objects.select_related('school').order_by('-id')[:5],
        'recent_students': Student.objects.select_related('school').order_by('-id')[:5]

    }
    return render(request, 'enrollment/index.html', {
        'school_count': context['school_count'],
        'course_count': context['courses_count'],
        'student_count': context['student_count'],
        'recent_course': context['recent_courses'],
        'recent_student': context['recent_students']
    })


def school_list(request):
    schools = School.objects.all().order_by('name')
    return render(request, 'enrollment/schools_list.html', {
        'schools': schools
    })

def courses_list(request):
    courses = Course.objects.all().order_by('name')
    return render(request, 'enrollment/courses_list.html', {'courses': courses})

def school_detail(request, slug):
    school = get_object_or_404(School, slug=slug)
    return render(request, 'enrollment/school_detail.html', {'school': school})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'enrollment/course_detail.html', {'course': course})

def students_list(request):
    students = Student.objects.all().order_by('student_name')
    return render(request, 'enrollment/students_list.html', {'students': students})

def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, 'enrollment/student_detail.html', {'student': student})
