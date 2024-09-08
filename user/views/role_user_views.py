from django.shortcuts import render,redirect, get_object_or_404
from ..forms import RoleUserForm

from user.models.role_user_model import RoleUserModel
 # Create your views here.


def role(request):
    role = RoleUserModel.objects.all()
    return render(request, 'users/users.html',{'role': role})


def add_role_view(request):

  if request.method =='POST':
     add_role =RoleUserForm(request.POST)
     if add_role.is_valid():
         print(add_role.cleaned_data)
         add_role.save()
     return redirect('users:index') 
  add_role = RoleUserForm()
  context = {'add_role':add_role}

  return render(request, 'users/add_users.html', context)





def edit_role_view(request, id):
    
     rolee = get_object_or_404(RoleUserModel, id=id)  
    
     if request.method == 'POST':
     
         if request.POST.get('action') == 'annuler':
             return redirect('users:index')   
        
        
         rolee = RoleUserModel(request.POST, instance=role)  
         if rolee.is_valid():
             rolee.save() 
             return redirect('users:index')  
     else:
      rolee = RoleUserForm(instance=role)  
    
     return render(request, 'users/edit_users.html', {'rolee': rolee})

 
   



   