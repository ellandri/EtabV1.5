from django.shortcuts import render
from django.contrib.auth.decorators import login_required






@login_required(login_url='dashboard:connect')
def reports_view(request):
    return render(request, 'reports/reports.html')
