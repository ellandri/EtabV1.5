from django.db import models
from user.models.user_model import UserModel

class RoleUserModel(models.Model):
    role = models.CharField(max_length=100)  
    users = models.ManyToManyField(UserModel, blank=True)  

    def __str__(self):
        return self.role
