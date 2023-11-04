from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('students')
    else:
        student_form = StudentForm()
    
    students_list = Student.objects.all()
    context = {'students_list': students_list, 'student_form': student_form}
    return render(request, 'myapp/students.html', context)

def courses(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('courses')
    else:
        course_form = CourseForm()
    
    courses_list = Course.objects.all()
    context = {'courses_list': courses_list, 'course_form': course_form}
    return render(request, 'myapp/courses.html', context)

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        if course_id:
            course = Course.objects.get(id=course_id)
            student.courses.add(course)
    
    courses_not_registered = Course.objects.exclude(students__id=student_id)
    context = {'student': student, 'courses_not_registered': courses_not_registered}
    return render(request, 'myapp/details.html', context)
