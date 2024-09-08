from django.urls import path
from teacher.views import teacher_view

app_name='teachers'
urlpatterns = [
    path('teachers/', teacher_view.teachers, name='index'),
    path('addt/', teacher_view.add_teachers , name='add'),
    path('editt/<int:id>/', teacher_view.edit_teachers_view, name='edit'),
    path('deletet/<int:id>/', teacher_view.delete_teachers_view, name='delete'),
    
]