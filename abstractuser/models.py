from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class CustomUser(AbstractBaseUser):
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )

    SERVICES = (
        ('am', 'Автомойка'),
        ('sm', 'Шиномонтаж'),
        ('re', 'Ремонт электрики'),
        ('kd', 'Компьютерная диагностика')
    )
    fio = models.CharField('ФИО', max_length=255, default='')
    car = models.CharField('Марка машины', max_length=255, default='Toyota')
    car_model = models.CharField('Модель автомобиля', max_length=255, default='Auris')
    phone_number = models.CharField('Номер телефона', max_length=255, default='+375445905077')
    service = models.CharField('Услуга', choices=SERVICES, max_length=255, default='')

    USERNAME_FIELD = "uid"

