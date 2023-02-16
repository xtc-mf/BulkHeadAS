from django import forms
from django.forms import ModelForm
from .models import *

class Entrollment(ModelForm):

    fio = forms.CharField(label="Фамилия Имя Отчество")
    car = forms.CharField(label="Автомобиль")
    car_model = forms.CharField(label="Модель")
    phone_number = forms.CharField(label="Номер телефона")
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    pub_order = forms.DateTimeField(label="Запись на")

    class Meta:
        model = Article
        fields = ["fio", "car", "car_model", "phone_number", "client_service", "pub_order"]
        labels = {'fio': 'ФИО', "car": "Марка автомобиля", "car_model": "Модель автомобиля", "phone_number": "Телефонный номер", "client_service": "Услуга", "pub_order": "Время записи"}
