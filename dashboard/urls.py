from django.urls import path

from .views import index, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name='dashboard'

urlpatterns = [
   path('', index, name='index'),
   path('con', CustomLoginView.as_view(), name='connect'),
   path('logout/', LogoutView.as_view(), name='logout'),


]