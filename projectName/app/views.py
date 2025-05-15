# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .forms import StudentForm
def index(request):
    context_variable = "Hello, world!"
    return render(request, 'index.html', {'context_variable': context_variable})


# views.py
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})



def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace with your actual URL name
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})
