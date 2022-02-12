from django.contrib import admin
from .models import Employee

class employeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'shift', 'team']


admin.site.register(Employee, employeeAdmin)