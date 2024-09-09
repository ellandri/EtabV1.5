from django.shortcuts import render,redirect, get_object_or_404
from ..forms import UserForm,RoleUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models.user_model import UserModel
from teacher.models.teacher_model import TeacherModel
from django.core.exceptions import ObjectDoesNotExist

from ..forms import RoleUserForm


# Create your views here.

@login_required(login_url='dashboard:connect')
def users_view(request):
    search_field = request.GET.get('search')
    if search_field :
        users = UserModel.objects.filter(username__icontains=search_field)
        context = {
            'users': users,
            'search_field': search_field,
        }
    else:
        users = UserModel.objects.all() 
        context = {
            'users': users,
        }
    return render(request, 'users/users.html',context)


def edit_users_view(request, id):  

    context = {
                "title": "modifier utilisateur"
    }
    
    user = get_object_or_404(UserModel, id=id)  
    
    if request.method == 'POST':
        if request.POST.get('action') == 'annuler':
            return redirect('users:index')   
       
        
        form = UserForm(request.POST, instance=user)  
        if form.is_valid():
            form.save()  
            return redirect('users:index') 
    else:
        form = UserForm(instance=user) 
    context["form"] = form
    
    return render(request, 'users/edit_users.html', context)

def add_users_view(request):
     
     if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if not username or not password:
           return render(request,'html/add_users.html')
        else:
           user = UserModel(username= username)
           user.save()
           user.password = password
           user.set_password(user.password)
           user.save()
           return redirect('users:index')
     add_role = RoleUserForm()
     user_form = UserForm()

     context = {
         'add_role' : add_role,
         'user_form': user_form
     }
     return render(request,'users/add_users.html',context)

        

#def add_users_view(request):
#    if request.method == "POST":
#        user_form = UserForm(request.POST)
#        add_role = RoleUserForm(request.POST)

#        if user_form.is_valid() and add_role.is_valid():
#            add_role = add_role.save()
#            user = user_form.save(commit=False)
#            user.role = add_role 
#            user.save()

#            messages.success(request, 'User added successfully!')
#            return redirect('users:index')
#        else:
#            messages.error(request, 'Please correct the errors below.')
#    else:
#        user_form = UserForm()
#        add_role = RoleUserForm()
#    return render(request, 'users/add_users.html', {'user_form': user_form, 'add_role': add_role})


def deactivate_user(request, user_id):
    user = get_object_or_404(UserModel, id=user_id)
    
    if user.is_active:
        user.is_active = False
        user.save()
        messages.success(request, f'L’utilisateur {user.username} a été désactivé avec succès.')
    else:
        messages.info(request, f'L’utilisateur {user.username} est déjà désactivé.')

    return redirect('users:index')