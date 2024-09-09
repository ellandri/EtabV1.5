from django.shortcuts import render,redirect, get_object_or_404
from ..forms import AbsenceModelForm
from django.contrib.auth.decorators import login_required
from student.models.absence_student_model import AbsenceModel



# Create your views here.


@login_required(login_url='dashboard:connect')
def absence_student(request):

   absences = AbsenceModel.objects.all() 
   return render(request, 'students/absence_student.html',{'absences':absences})


def add_absence_student(request):

 if request.method =='POST':
    add_form = AbsenceModelForm(request.POST)
    if add_form.is_valid():
      print(add_form.cleaned_data)
      add_form.save()
    return redirect('absence:index')
 add_form = AbsenceModelForm()
 context = {'add_form':add_form}

 return render(request, 'students/add_absence_student.html',context)






def edit_absence_student(request, id):
    
    absence = get_object_or_404(AbsenceModel, id=id)  
    
    if request.method == 'POST':
     
        if request.POST.get('action') == 'annuler':
            return redirect('absence:index')   
        
        
        form = AbsenceModelForm(request.POST, instance=absence)  
        if form.is_valid():
            form.save() 
            return redirect('absence:index')  
    else:
     form = AbsenceModelForm(instance=absence)  
    
    return render(request, 'students/edit_absence_student.html', {'form': form})

 
   


def delete_absence_student(request, id):
    absence = get_object_or_404(AbsenceModel, id=id)  
  
    absence.delete()
   
    return redirect('absence:index')

   