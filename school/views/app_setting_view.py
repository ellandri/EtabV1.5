from django.shortcuts import render,redirect, get_object_or_404
from ..forms import SchoolForm, AppSettingForm
from school.models.app_setting_model import  AppSettingModel
from django.contrib import messages

#@login_required(login_url='dashboard:connect')

def app(request):
  # students = Students.objects.filter(is_deleted=False)
   apps = AppSettingModel.objects.all() 
   return render(request, 'schools/app.html',{'apps':apps})



def add_app(request):

    if request.method == "POST":
        app_form = AppSettingForm(request.POST)

        if app_form.is_valid():
            app_form.save()

            messages.success(request, 'App added successfully!')
            return redirect('school:check_school')  
        else:
            print('gggggg')
            messages.error(request, 'Please correct the errors below.')
    else:
        app_form = AppSettingForm()

    return render(request, 'schools/conn/add_app.html', {'app_form': app_form})






def edit_app(request, id):
    
    app = get_object_or_404(AppSettingModel, id=id)  

    
    if request.method == "POST":
        app_form = AppSettingForm(request.POST, instance=app)

        if app_form.is_valid():
        
            app_form = app_form.save()
            app.save()

            messages.success(request, 'App setting added successfully!')
            return redirect('app:index')
        else:
            print('gggggg')
            messages.error(request, 'Please correct the errors below.')
    else:
        app_form = AppSettingForm(instance=app)

    return render(request, 'schools/edit_app.html', {'app_form': app_form})



def delete_app(request, id):
    app = get_object_or_404(AppSettingModel, id=id)  
    app_setting = get_object_or_404(AppSettingModel,id=app.id)
    app_setting.delete()

    return redirect('app:index')

def check_settings(request):
    apps = AppSettingModel.objects.all()
    if not apps:
        return redirect('app:add')
    else:
        return redirect('school:index')
    
