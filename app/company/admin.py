from django.contrib import admin

from .models import Department, Employee

admin.site.register(Employee)
admin.site.register(Department)
