from django import forms
from student.models.student_model import StudentModel
from student.models.absence_student_model import AbsenceModel
from student.models.student_cards_model import StudentCards

class StudentsForm(forms.ModelForm):
 class Meta:
    model= StudentModel
    fields="__all__"
    exclude = ("address","status",)


class AbsenceModelForm(forms.ModelForm):
  
  class Meta:
    model= AbsenceModel
    fields= ["student","absence_date","absence_number"]
    widgets = {
      'absence_date':forms.DateInput(attrs={'type':'date'})
    }
    

class StudentsCardsModelForm(forms.ModelForm):
  class Meta:
    model= StudentCards
    fields= ["student","reference","expiration_date","issue_date"]

    widgets = {
      'expiration_date':forms.DateInput(attrs={'type':'date'}),
      'issue_date':forms.DateInput(attrs={'type':'date'})
    }
    