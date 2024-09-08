import openpyxl
from django.http import HttpResponse
from student.models.student_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from user.models.user_model import UserModel

def generate_excel_report(request):
    report_type = request.GET.get('option')

    if report_type == 'students':
        data = StudentModel.objects.all()
    elif report_type == 'teachers':
        data = TeacherModel.objects.all()
    elif report_type == 'users':
        data = UserModel.objects.all()
    else:
        return HttpResponse("Type de rapport invalide", status=400)

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    if report_type == 'students':
        sheet.append(['first_name', 'last_name', 'matricule', 'birthday'])
        for student in data:
            sheet.append([student.first_name, student.last_name, student.matricule, student.birthday])
    elif report_type == 'teachers':
        sheet.append(['first_name', 'last_name', 'specialty'])
        for teacher in data:
            sheet.append([teacher.first_name, teacher.last_name, teacher.specialty])
    elif report_type == 'users':
        sheet.append(['Nom d’utilisateur', 'Email'])
        for user in data:
            sheet.append([user.username, user.email])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={report_type}_report.xlsx'
    workbook.save(response)
    return response
