from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserModel(AbstractUser, DateTimeModel):
    school = models.ForeignKey(
        'school.SchoolModel', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    role = models.ManyToManyField(
        'user.RoleUserModel', 
        blank=True  
    )
    username = models.CharField(max_length=255, unique=True) 
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  
        blank=True,
    )

    def __str__(self):
        return self.username
