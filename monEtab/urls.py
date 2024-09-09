"""
URL configuration for monEtab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dashboard.views import index

urlpatterns = [
    path('api/', include("api.urls")),
    path('school/',include("school.urls.school_urls")),
    path('',include("school.urls.app_setting_urls")),
    path('admin/', admin.site.urls),
    path('dashoard',include("dashboard.urls")),
    path('students/',include("student.urls.student_urls")),
    path('studenta/',include("student.urls.absence_student_urls")),
    path('studentc/',include("student.urls.student_cards_urls")),
    path('users/',include("user.urls")),
    path('reports/',include("report.urls")),
    path('teacher/',include("teacher.urls")),
    
]
