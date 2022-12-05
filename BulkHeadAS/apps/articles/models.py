from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class Services(models.Model):
    service_name = models.CharField('Название услуги', max_length=50, default='')
    #service_time_work = models.IntegerField('Примерное время работы')
    #service_employee = models.CharField('00Фамилия работника', max_length=50)

    def __str__(self):
        return self.service_name
    class Meta:

        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Article(models.Model):


    SERVICES = (
       ('am', 'Автомойка'),
       ('sm', 'Шиномонтаж'),
       ('re', 'Ремонт электрики'),
       ('kd', 'Компьютерная диагностика')
    )




   # login = models.CharField('Логин', max_length=255, default='123123123')

    fio = models.CharField('ФИО', max_length=255, default='Рубец Алексей Сергеевич')
    car = models.CharField('Марка машины', max_length=255, default='Toyota')
    car_model = models.CharField('Модель автомобиля', max_length=255, default='Auris')
    phone_number = models.CharField('Номер телефона', max_length=255, default='+375445905077')
    service = models.CharField('Услуга', choices=SERVICES, max_length=255, default='')
    pub_order = models.DateTimeField('Дата заказа')
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default='0')

    objects = UserManager()

    USERNAME_FIELD = 'fio'
    REQUIRED_FIELDS = ['username']

    def __str__ (self):
        return self.fio

    class Meta:
        verbose_name = 'КЛИЕНТОВ'
        verbose_name_plural = 'Клиент'

