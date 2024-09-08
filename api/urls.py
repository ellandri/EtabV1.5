from django.urls import path
from api.api_views.student_api_views import student_list
from api.api_views.teacher_api_views import teacher_list


urlpatterns = [
    path('',student_list),
    path('teacher',teacher_list),
]
