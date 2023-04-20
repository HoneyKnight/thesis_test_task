# Generated by Django 4.2 on 2023-04-20 16:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название компании')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(db_index=True, max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('photo', models.ImageField(upload_to='employees/photos/', verbose_name='Фото')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Зарплата не может быть ниже 0')], verbose_name='Зарплата')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Возраст не может быть ниже года'), django.core.validators.MaxValueValidator(200, 'Столько люди пока не живут')], verbose_name='Возраст')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.department')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_departments', to='company.employee'),
        ),
    ]