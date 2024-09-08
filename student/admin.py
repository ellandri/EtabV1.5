from django.contrib import admin
from student.models.student_model import StudentModel
from student.models.student_cards_model import StudentCards
from student.models.absence_student_model import AbsenceModel


# Register your models here.

admin.site.register(StudentModel)
admin.site.register(StudentCards)
admin.site.register(AbsenceModel)