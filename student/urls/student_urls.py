from django.urls import path
from ..views import student_view

app_name='students'

urlpatterns = [
   path('students/', student_view.students, name='index'),
   path('adds/', student_view.add_students_view, name='add'),
   path('edits/<int:id>/', student_view.edit_students_view, name='edit'),
   path('deletes/<int:id>/', student_view.delete_students_view, name='delete'),
    
]