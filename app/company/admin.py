from django.contrib import admin

from .models import Department, Employee, Projects


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    filter_horizontal = ('employees',)


admin.site.register(Employee)
admin.site.register(Department)
