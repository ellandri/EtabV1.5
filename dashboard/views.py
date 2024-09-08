from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='dashboard:connect')

def index(request):
    return render(request, "dashboard/dashboard.html")


class CustomLoginView(LoginView):
    template_name = 'dashboard/connect.html'
    success_url = 'dashboard'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:index')  # Redirige si l'utilisateur est connecté
        return super().dispatch(request, *args, **kwargs)



#def connect_view(request):
   # return render(request, 'html/connect.html')
