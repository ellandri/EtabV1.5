from django.shortcuts import render,redirect, get_object_or_404
from ..forms import SchoolForm, AppSettingForm
from school.models.school_model import  SchoolModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required







@login_required(login_url='dashboard:connect')
def school(request):
  # students = Students.objects.filter(is_deleted=False)
   schools = SchoolModel.objects.all() 
   return render(request, 'schools/school.html',{'schools':schools})



def add_school(request):

    if request.method == "POST":
        school_form = SchoolForm(request.POST)

        if school_form.is_valid():
            school_form.save()

            messages.success(request, 'School added successfully!')
            return redirect('dashboard:connect')
        else:
            print('gggggg')
            messages.error(request, 'Please correct the errors below.')
    else:
        school_form = SchoolForm()

    return render(request, 'schools/add_school.html', {'school_form': school_form})







def edit_school(request, id):
    
    school = get_object_or_404(SchoolModel, id=id)  

    
    if request.method == "POST":
        school_form = SchoolForm(request.POST, instance=school)

        if school_form.is_valid():
        
            school_form = school_form.save()
            school.save()

            messages.success(request, 'School added successfully!')
            return redirect('school:index')
        else:
            print('gggggg')
            messages.error(request, 'Please correct the errors below.')
    else:
        school_form = SchoolForm(instance=school)

    return render(request, 'schools/edit_school.html', {'school_form': school_form})



def delete_school_(request, id):
    school = get_object_or_404(SchoolModel, id=id)  
    school.delete()

    return redirect('school:index')


def check_school(request):
    schools = SchoolModel.objects.all()
    if not schools:
        return redirect('school:add')
    else:
        return redirect('dashboard:connect')
    
