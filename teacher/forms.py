from django import forms
from teacher.models.teacher_model import TeacherModel



class TeachersForm(forms.ModelForm):

 class Meta:
        model = TeacherModel
        fields="__all__"

       


 