# Generated by Django 4.1.2 on 2023-02-26 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_employee_alter_article_car_alter_article_fio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]