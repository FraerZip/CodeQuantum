from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),

]