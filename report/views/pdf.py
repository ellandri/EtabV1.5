from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from student.models.student_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from user.models.user_model import UserModel


def generate_pdf_report(request):
    report_type = request.GET.get('option')

    if report_type == 'students':
        data = StudentModel.objects.all()
        template = 'reports/student_pdf.html'
    elif report_type == 'teachers':
        data = TeacherModel.objects.all()
        template = 'reports/teacher_pdf.html'
    elif report_type == 'users':
        data = UserModel.objects.all()
        template = 'reports/user_pdf.html'
    else:
        return HttpResponse("Type de rapport invalide", status=400)

    html = render_to_string(template, {'data': data})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={report_type}_report.pdf'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Erreur lors de la création du PDF', status=400)

    return response
