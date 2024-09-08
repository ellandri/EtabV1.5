from django import forms
from user.models.user_model import UserModel as User
from user.models.role_user_model import  RoleUserModel as RoleUser

   
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ["username","password","school"]
       
       
class RoleUserForm(forms.ModelForm):
        class Meta:
            model = RoleUser
            fields = ["role"]  