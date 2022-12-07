from django import forms
from django.forms import ModelForm
from .models import *

class Entrollment(ModelForm):

    fio = forms.CharField()
    car = forms.CharField()
    car_model = forms.CharField()
    phone_number = forms.CharField()
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    pub_order = forms.DateTimeField()

    class Meta:
        model = Article
        fields = ["fio", "car", "car_model", "phone_number", "client_service", "pub_order"]
        labels = {"fio": "ФИО", "car": "Марка автомобиля", "car_model": "Модель автомобиля", "phone_number": "Телефонный номер", "client_service": "Услуга", "pub_order": "Время записи"}
    #
    #client_service = forms.ForeignKey(Services, on_delete=models.CASCADE)



    #pub_order = forms.DateTimeField(initial='Дата заказа')
    #choose = forms.ChoiceField('Услуга', choices=SERVICES, widget=forms.Select)
    #