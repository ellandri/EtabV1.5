from django.urls import path
from .views import user_views


app_name='users'
urlpatterns = [
    path('users/', user_views.users_view, name='index'),
    path('addu/', user_views.add_users_view, name='add'),
    path('editu/<int:id>/', user_views.edit_users_view, name='edit'),
    path('users/deactivate/<int:user_id>/', user_views.deactivate_user, name='deactivate_user'),
]
