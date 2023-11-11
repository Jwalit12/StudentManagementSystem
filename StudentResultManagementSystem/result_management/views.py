# result_management/views.py
from .models import Student, Course, Result
from django.shortcuts import render, redirect
from .forms import StudentForm, CourseForm, ResultForm
from django.contrib import messages

def home(request):
    return render(request, 'result_management/home.html')

from datetime import datetime, timedelta

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('add_student')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    # Calculate max_birth_date
    current_date = datetime.now().date()
    max_birth_date = (current_date - timedelta(days=10*365)).isoformat()

    return render(request, 'result_management/add_student.html', {'form': form,  'max_birth_date': max_birth_date})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'result_management/student_list.html', {'students': students})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_list')

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully.')
            return redirect('add_course')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CourseForm()

    return render(request, 'result_management/add_course.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'result_management/course_list.html', {'courses': courses})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    messages.success(request, 'Course deleted successfully.')
    return redirect('course_list')

def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result added successfully.')
            return redirect('add_result')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ResultForm()

    return render(request, 'result_management/add_result.html', {'form': form})

def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_management/result_list.html', {'results': results})