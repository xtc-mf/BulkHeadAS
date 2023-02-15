import datetime
from django.utils import timezone
from django.db import models

class Services(models.Model):
    service_name = models.CharField('Название услуги', max_length=50, default='')
    def __str__(self):
        return self.service_name
    class Meta:

        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Article(models.Model):

    fio = models.CharField('ФИО', max_length=255, default='Рубец Алексей Сергеевич')
    car = models.CharField('Марка машины', max_length=255, default='Toyota')
    car_model = models.CharField('Модель автомобиля', max_length=255, default='Auris')
    phone_number = models.CharField('Номер телефона', max_length=255, default='+375445905077')
    pub_order = models.DateTimeField('Дата заказа')
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)

    USERNAME_FIELD = 'fio'
    REQUIRED_FIELDS = ['username']

    def __str__ (self):
        return self.fio
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
