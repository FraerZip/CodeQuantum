from django.shortcuts import render, redirect
from .models import Courses
from .forms import CoursesForm

def courses_home(request):
    course = Courses.objects.all()
    return render(request, 'courses/courses.html', {'course': course})

def create_course(request):
    error = ''
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверно заполнена!'

    form = CoursesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'courses/create_course.html', data)