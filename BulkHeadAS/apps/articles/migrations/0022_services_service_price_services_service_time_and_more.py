# Generated by Django 4.1.2 on 2023-02-23 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_remove_article_номер телефона_article_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='services',
            name='service_time',
            field=models.IntegerField(default=1, verbose_name='Примерное время'),
        ),
        migrations.AlterField(
            model_name='article',
            name='phone_number',
            field=models.CharField(help_text="Телефонный номер должен быть в форме: '+375(17/25/29/33/44)XXXXXXX'.", max_length=20, validators=[django.core.validators.RegexValidator('\\+375(17|29|25|33|44)[0-9]{7}')], verbose_name='Телефонный номер'),
        ),
    ]
