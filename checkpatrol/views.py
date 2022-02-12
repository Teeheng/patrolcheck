from django.http import HttpResponse
from django.shortcuts import render
from database.models import Employee,EmployeeForm

def index(request):
    return render(request, 'index.html')

def input(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()        
    return render(request, 'input.html', {'form': form})

def review(request):
    data = Employee.objects.all()
    return render(request, 'read-data.html', {'data': data})
