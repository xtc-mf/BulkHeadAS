# Generated by Django 4.1.2 on 2023-02-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_employee_employee_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_rank',
            field=models.CharField(default='', max_length=25, verbose_name='Должность'),
        ),
    ]