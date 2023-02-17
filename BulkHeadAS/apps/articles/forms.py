from django import forms
from django.forms import ModelForm
from .models import *

phone_regex = r'\+375(17|29|25|33|44)[1-9]{7}'
regex_error = 'Телефонный номер должен быть в формате: +375(17/25/29/33/44)1234567.'

CARS = [
    ('Toyota', (('C-HR', 'C-HR'), ('Sai', 'Sai'), ('Auris', 'Auris'), ('Prius', 'Prius'), ('Land Cruiser', 'Land Cruiser'),
        ('Avensis', 'Avensis'), ('Camry', 'Camry'), ('Highlander', 'Highlander'), ('RAV4', 'RAV4'), ('Crown', 'Crown')
    )
     ),
]

class Entrollment(ModelForm):

    fio = forms.CharField(label="Фамилия Имя Отчество")
    car = forms.ChoiceField(choices = CARS, label='Автомобиль')
    phone_number = forms.RegexField(regex=phone_regex,
                                    label='Номер телефона',
                                    help_text="Телефонный номер должен быть в формате: +375(17/25/29/33/44)XXXXXXX."
                                    )
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    pub_order = forms.DateTimeField(label="Запись на")

    class Meta:
        model = Article
        fields = ["fio", "car", "phone_number", "client_service", "pub_order"]
        labels = {'fio': 'ФИО', "car": "Автомобиль", "phone_number": "Телефонный номер", "client_service": "Услуга", "pub_order": "Время записи"}
