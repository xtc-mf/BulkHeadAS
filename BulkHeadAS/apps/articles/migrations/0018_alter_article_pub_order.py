# Generated by Django 4.1.2 on 2023-01-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_alter_article_pub_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_order',
            field=models.DateTimeField(verbose_name='Дата заказа'),
        ),
    ]
