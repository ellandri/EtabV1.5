from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='dashboard:connect')
def index(request):
    return render(request, "dashboard/dashboard.html")

class CustomLoginView(LoginView):
    template_name = 'dashboard/connect.html'
    success_url = 'dashboard'



#def connect_view(request):
   # return render(request, 'html/connect.html')

