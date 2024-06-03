from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('create_course', views.create_course, name='create_course'),
    path('<int:pk>', views.CoursesDetailView.as_view(), name='course-detail'),
    path('<int:pk>/update', views.CoursesUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete', views.CoursesDeleteView.as_view(), name='course-delete'),
]