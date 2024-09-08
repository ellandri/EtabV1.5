from django.shortcuts import render,redirect, get_object_or_404
from ..forms import TeachersForm
from teacher.models.teacher_model import  TeacherModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='dashboard:connect')
def teachers(request):
    search_field = request.GET.get('search')
    if search_field :
        teachers = TeacherModel.objects.filter(last_name__icontains=search_field )| TeacherModel.objects.filter(first_name__icontains=search_field )
        context = {
            'teachers': teachers,
            'search_field': search_field,
        }
    else:
        teachers = TeacherModel.objects.all() 
        context = {
            'teachers':teachers,
        }
    return render(request, 'teachers/teachers.html',context)


def add_teachers(request):

    if request.method == 'POST':
    
        prof_form = TeachersForm(request.POST)
  
        if prof_form.is_valid():
            print(prof_form.cleaned_data)
            prof_form.save()
        return redirect('teachers:index')   
    prof_form = TeachersForm()
    context = {'prof_form':prof_form}
    return render(request, 'teachers/add_teachers.html',context)



def edit_teachers_view(request, id):  

    teacher = get_object_or_404(TeacherModel, id=id)  
    
    if request.method == 'POST':
     if request.POST.get('action') == 'annuler':
      return redirect('teachers:index')   
       
        
    form = TeachersForm(request.POST, instance=teacher)  
    if form.is_valid():
        form.save()  
        return redirect('teachers:index') 
    else:
     form = TeachersForm(instance=teacher) 
    
    return render(request, 'teachers/edit_teachers.html', {'form': form})



def delete_teachers_view(request, id):
    teacher = get_object_or_404(TeacherModel, id=id)  
    teacher.delete() 
    
    return redirect('teachers:index')

