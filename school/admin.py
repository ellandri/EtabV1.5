from django.contrib import admin
from school.models.school_model import SchoolModel
from school.models.app_setting_model import AppSettingModel

# Register your models here.

admin.site.register(SchoolModel)
admin.site.register(AppSettingModel)