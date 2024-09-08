from django.urls import path
from ..views import student_card_view 

app_name='cards'

urlpatterns = [
   path('cards/', student_card_view .student_cards, name='index'),
   path('carda/', student_card_view .add_student_cards, name='add'),
   path('cardedit/<int:id>/', student_card_view .edit_student_cards, name='edit'),
   path('deletes/<int:id>/', student_card_view .delete_student_cards, name='delete'),
    
]