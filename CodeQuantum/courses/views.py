from django.shortcuts import render, redirect
from .models import Courses
from .forms import CoursesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def courses_home(request):
    course = Courses.objects.all()
    return render(request, 'courses/courses.html', {'course': course})

class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'courses/details_view.html'
    context_object_name = 'course'

class CoursesUpdateView(UpdateView):
    model = Courses
    template_name = 'courses/create_course.html'

    form_class = CoursesForm

class CoursesDeleteView(DeleteView):
    model = Courses
    template_name = 'courses/courses_confirm_delete.html'
    success_url = '/courses/'


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