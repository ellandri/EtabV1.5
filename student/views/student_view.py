from django.shortcuts import render,redirect, get_object_or_404
from student.forms import StudentsForm
from base.forms import AdressForm
from student.models.student_model import StudentModel
from base.models.address_model import AddressModel

from django.contrib import messages
# Create your views here.



def students(request):
    search_field = request.GET.get('search')
    if search_field :
        students = StudentModel.objects.filter(last_name__icontains=search_field )| StudentModel.objects.filter(first_name__icontains=search_field )
        context = {
            'students': students,
            'search_field': search_field,
        }
    else:
        students = StudentModel.objects.all() 
        context = {
            'students':students,
        }
    return render(request, 'students/students.html',context)






def add_students_view(request):

    if request.method == "POST":
        student_form = StudentsForm(request.POST)
        adress_form = AdressForm(request.POST)

        if student_form.is_valid() and adress_form.is_valid():
            adress = adress_form.save()

           
            student = student_form.save(commit=False)
            student.address = adress
            student.save()

            messages.success(request, 'Student added successfully!')
            return redirect('students:index')
        else:
            print('gggggg')
            messages.error(request, 'Please correct the errors below.')
    else:
        student_form = StudentsForm()
        adress_form = AdressForm()

    return render(request, 'students/add_students.html', {'student_form': student_form, 'adress_form': adress_form})







def edit_students_view(request, id):
    
    student = get_object_or_404(StudentModel, id=id)  
    
    if request.method == 'POST':
     
        if request.POST.get('action') == 'annuler':
            return redirect('students:index')   
        
        
        form = StudentsForm(request.POST, instance=student)  
        if form.is_valid():
            form.save() 
            return redirect('students:index')  
    else:
     form = StudentsForm(instance=student)  
    
    return render(request, 'students/edit_students.html', {'form': form})

 
   


def delete_students_view(request, id):
    student = get_object_or_404(StudentModel, id=id)  
   # student.is_deleted = True
    student.delete()
    #student.save()
    return redirect('students:index')

   