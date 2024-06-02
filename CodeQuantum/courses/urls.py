from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('create_course', views.create_course, name='create_course'),
    path('courses', views.create_course, name='create_course'),
]