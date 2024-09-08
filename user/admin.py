from django.contrib import admin
from user.models.user_model import UserModel
from user.models.role_user_model import RoleUserModel
from django.contrib.auth.admin import UserAdmin



# Register your models here.

@admin.register(UserModel)
class Utilisateur(UserAdmin):
    pass

admin.site.register(RoleUserModel)