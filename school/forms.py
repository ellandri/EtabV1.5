from django import forms
from school.models.school_model import SchoolModel
from school.models.app_setting_model import AppSettingModel



class AppSettingForm(forms.ModelForm):
  class Meta:
     model= AppSettingModel

     fields=["smpt_server","smpt_port", "smpt_username","smpt_password"]





class SchoolForm(forms.ModelForm):
 class Meta:
    model= SchoolModel

    fields=["name","url_logo"]
   
