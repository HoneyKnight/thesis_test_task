from rest_framework import serializers

from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField()
    employees_total_salary = serializers.IntegerField()

    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'director',
            'employees_count',
            'employees_total_salary',
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'photo',
            'position',
            'salary',
            'age',
            'department',
        )
