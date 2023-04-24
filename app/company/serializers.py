from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Department, Employee, Projects


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
        validators = [
            UniqueTogetherValidator(
                queryset=Employee.objects.all(),
                fields=['first_name', 'last_name'],
                message='Такой сотрудник уже есть'
            )
        ]


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = (
            'id',
            'name',
        )


class ProjectsRetrieveSerializer(serializers.ModelSerializer):
    director = EmployeeSerializer()
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Projects
        fields = '__all__'
