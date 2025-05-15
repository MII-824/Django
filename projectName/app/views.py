# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# views.py
from django.shortcuts import render
from .models import Student
from django.db.models import Q
from .forms import StudentForm

def index(request):
    context_variable = "Hello, world!"
    return render(request, 'index.html', {'context_variable': context_variable})




def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()
    if query:
        students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))
    return render(request, 'students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Replace with your student list URL name
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

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

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')  # Replace with your list view name
