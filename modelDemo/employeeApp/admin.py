from django.contrib import admin
from employeeApp.models import Employee

# Register your models here.
class EmployeeName(admin.ModelAdmin):
    list_display = ['firstName', 'lastName']
    
admin.site.register(Employee, EmployeeName)
