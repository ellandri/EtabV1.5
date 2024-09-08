from django.urls import path
from report.views.report import reports_view
from report.views.pdf import generate_pdf_report
from report.views.exel import generate_excel_report

app_name = 'reports'

urlpatterns = [
    path('', reports_view, name='report'),  # Cette URL sera : /reports/
    path('generate-pdf/', generate_pdf_report, name='generate_pdf'),  # Cette URL sera : /reports/generate-pdf/
    path('generate-excel/', generate_excel_report, name='generate_excel'),  # Cette URL sera : /reports/generate-excel/
]
