from django.shortcuts import render,redirect, get_object_or_404
from ..forms import StudentsCardsModelForm
from django.contrib.auth.decorators import login_required
from student.models.student_cards_model import StudentCards



# Create your views here.


@login_required(login_url='dashboard:connect')
def student_cards(request):
  # students = Students.objects.filter(is_deleted=False)
   cards = StudentCards.objects.all() 
   return render(request, 'students/student_cards.html',{'cards':cards})


def add_student_cards(request):

 if request.method =='POST':
    add_form = StudentsCardsModelForm(request.POST)
    if add_form.is_valid():
      print(add_form.cleaned_data)
      add_form.save()
      return redirect('cards:index')
 add_form = StudentsCardsModelForm()
 context = {'add_form':add_form}

 return render(request, 'students/add_absence_student.html',context)






def edit_student_cards(request, id):
    
    card = get_object_or_404( StudentCards, id=id)  
    
    if request.method == 'POST':
     
        if request.POST.get('action') == 'annuler':
            return redirect('cards:index')   
        
        
        form =StudentsCardsModelForm(request.POST, instance=card)  
        if form.is_valid():
            form.save() 
            return redirect('cards:index')  
    else:
        form = StudentsCardsModelForm(instance=card)  
    
    return render(request, 'students/edit_student_cards.html', {'form': form})

 
   


def delete_student_cards(request, id):
    cards = get_object_or_404(StudentCards, id=id)  
  
    cards.delete()
   
    return redirect('cards:index')

   