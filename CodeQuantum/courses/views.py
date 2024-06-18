from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses, Lesson
from .forms import CoursesForm, LessonForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

@login_required(login_url='user:login')
def courses_home(request):
    course = Courses.objects.all()
    return render(request, 'courses/courses.html', {'course': course})

@login_required(login_url='user:login')
def web_developer(request):
    course = Courses.objects.all()
    return render(request, 'courses/web_developer.html', {'course': course})

@login_required(login_url='user:login')
def python_developer(request):
    course = Courses.objects.all()
    return render(request, 'courses/python_developer.html', {'course': course})

@login_required(login_url='user:login')
def java_developer(request):
    course = Courses.objects.all()
    return render(request, 'courses/java_developer.html', {'course': course})

@login_required(login_url='user:login')
def lesson_python_hello(request):
    course = Courses.objects.all()
    return render(request, 'courses/lesson_python_hello.html', {'course': course})

@login_required(login_url='user:login')
def lesson_python_begin(request):
    course = Courses.objects.all()
    return render(request, 'courses/lesson_python_begin.html', {'course': course})

@login_required(login_url='user:login')
def lesson_python_instruction(request):
    course = Courses.objects.all()
    return render(request, 'courses/lesson_python_instruction.html', {'course': course})


class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'courses/details_view.html'
    context_object_name = 'course'


@method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='user:login'), name='dispatch')
class CoursesUpdateView(UpdateView):
    model = Courses
    template_name = 'courses/create_course.html'
    form_class = CoursesForm


@method_decorator(user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='user:login'), name='dispatch')
class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'courses/courses_confirm_delete.html'
    success_url = reverse_lazy('courses:courses_home')

def is_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_admin, login_url='user:login')
def create_course(request):
    error = ''
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:courses_home')
        else:
            error = 'Форма неверно заполнена!'

    form = CoursesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'courses/create_course.html', data)

@user_passes_test(is_admin, login_url='user:login')
def create_lesson(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('courses:course-detail', pk=course.id)
    else:
        form = LessonForm()
    return render(request, 'courses/create_lesson.html', {'form': form, 'course': course})