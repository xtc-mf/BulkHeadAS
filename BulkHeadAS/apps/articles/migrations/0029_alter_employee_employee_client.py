# Generated by Django 4.1.2 on 2023-02-26 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0028_alter_employee_employee_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]
