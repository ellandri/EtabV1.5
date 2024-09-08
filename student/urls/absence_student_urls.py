from django.urls import path
from ..views import absence_student_view 

app_name='absence'

urlpatterns = [
   path('absence/', absence_student_view.absence_student, name='index'),
   path('addt/', absence_student_view.add_absence_student, name='add'),
   path('editss/<int:id>/', absence_student_view.edit_absence_student, name='edit'),
   path('deletesa/<int:id>/', absence_student_view.delete_absence_student, name='delete'),
    
]