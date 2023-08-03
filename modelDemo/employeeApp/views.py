from django.shortcuts import render
from employeeApp.models import Employee

# Create your views here.
def displayEmployee(request):
    employeeDetails = Employee.objects.all()
    employeeDict = {
        "employees" : employeeDetails,
    }
    return render(request, 'empApp/employee.html', employeeDict)
