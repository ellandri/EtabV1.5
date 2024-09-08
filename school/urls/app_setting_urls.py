from django.urls import path
from school.views.app_setting_view import app, add_app, edit_app, delete_app,check_settings

app_name = 'app'
urlpatterns = [
    path('', check_settings, name='check_settings'),
    path('app/', app, name='index'),
    path('addapp/', add_app, name='add'),
    path('editapp/<int:id>/', edit_app, name='edit'),
    path('deleteapp/<int:id>/', delete_app, name='delete'),
]
