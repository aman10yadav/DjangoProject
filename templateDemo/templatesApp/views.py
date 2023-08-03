from django.shortcuts import render

# Create your views here.

def displayTemplate(request):
    mydict = {
        "name" : "Mock_name"
    }
    return render(request, 'templatesApp/index.html', context=mydict)


def displayEmployees(request):
    mydict = {
        "id" : 101,
        "name" : "Mock_name",
        "salary" : 10000
    }
    return render(request, "templatesApp/employeeTemplates.html", mydict)
