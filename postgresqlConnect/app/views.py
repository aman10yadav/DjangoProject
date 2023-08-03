from django.shortcuts import render
from .models import Student

# Create your views here.

def index(request):
    obj = Student.objects.all()
    context = {
        "obj": obj,
    }
    print("objs => ", obj)
    print("context => ", context)
    return render(request, "index.html", context)
