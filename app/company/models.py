from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Department(models.Model):
    name = models.CharField('Название компании', max_length=255)
    director = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='managed_departments',
    )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255, db_index=True)
    patronymic = models.CharField('Отчество', max_length=255)
    photo = models.ImageField('Фото', upload_to='employees/photos/')
    position = models.CharField('Должность', max_length=255)
    salary = models.IntegerField(
        'Зарплата',
        validators=[
            MinValueValidator(0, message='Зарплата не может быть ниже 0')
        ]
    )
    age = models.IntegerField(
        'Возраст',
        validators=[
            MinValueValidator(1, message='Возраст не может быть ниже года'),
            MaxValueValidator(200, 'Столько люди пока не живут')
        ]
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self) -> str:
        return (
            f'{self.last_name} {self.first_name}'
            f'{self.patronymic} | {self.position}'
        )


class Projects(models.Model):
    name = models.CharField('Название проекта', max_length=255)
    director = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='managed_projects'
    )
    employees = models.ManyToManyField(
        Employee,
        'Сотрудники',
        # related_name='managed_employees',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self) -> str:
        return self.name
