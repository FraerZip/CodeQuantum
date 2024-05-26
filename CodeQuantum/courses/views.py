from django.shortcuts import render
from .models import Courses


def courses_home(request):
    course = Courses.objects.all()
    return render(request, 'courses/courses.html', {'course': course})
