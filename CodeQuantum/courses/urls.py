from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('create_course', views.create_course, name='create_course'),
    path('web_developer', views.web_developer, name='web_developer'),
    path('python_developer', views.python_developer, name='python_developer'),
    path('java_developer', views.java_developer, name='java_developer'),
    path('lesson_python_hello', views.lesson_python_hello, name='lesson_python_hello'),
    path('lesson_python_begin', views.lesson_python_begin, name='lesson_python_begin'),
    path('lesson_python_instruction', views.lesson_python_instruction, name='lesson_python_instruction'),
    path('<int:pk>', views.CoursesDetailView.as_view(), name='course-detail'),
    path('<int:pk>/update', views.CoursesUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete', views.CoursesDeleteView.as_view(), name='course-delete'),
    path('<int:course_id>/lesson/create/', views.create_lesson, name='create_lesson'),
]