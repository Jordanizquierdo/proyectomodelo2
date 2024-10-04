from django.shortcuts import render
from app1.models import Employee
from . import forms

def employeeData(request):
    empleados=Employee.objects.all()
    data = {'empleados': empleados}
    return render(request,'app/empleados.html',data)


def UserRegistrationView(request):
    form = forms.UserRegistrarForm()
    data={'form':form}
    return render(request, 'User.html',data)


