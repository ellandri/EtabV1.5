from django.db import models

from base.models.person_model import PersonModel


class StudentModel(PersonModel):
    
    matricule = models.CharField(max_length=255)
    phone_number_father = models.CharField(max_length=20)


    def __str__(self) :
      return f"{self.first_name} {self.last_name} "


