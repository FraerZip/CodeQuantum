from django.shortcuts import render

def courses_home(request):
    return render(request, 'main/courses.html')
