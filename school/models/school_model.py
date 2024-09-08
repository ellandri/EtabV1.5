from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

class SchoolModel(DateTimeModel):
    app_setting = models.OneToOneField('school.AppSettingModel', on_delete=models.SET_NULL, null=True, related_name="school_app_setting_id")
    name = models.CharField(max_length=50)
    url_logo = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name