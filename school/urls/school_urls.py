from django.urls import path
from school.views.school_view import school, add_school, edit_school,delete_school_, check_school

app_name='school'
urlpatterns = [
    path('', check_school, name='check_school'),
    path('schools/', school, name='index'),
    path('addschool/', add_school, name='add'),
    path('editschool/<int:id>/', edit_school, name='edit'),
    path('deleteschool/<int:id>/', delete_school_, name='delete'),
    
]