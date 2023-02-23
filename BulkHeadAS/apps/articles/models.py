import datetime
from django.utils import timezone
import re
from django.core.validators import RegexValidator
from django.db import models

CARS = [
    ('Toyota', (('C-HR', 'C-HR'), ('Sai', 'Sai'), ('Auris', 'Auris'), ('Prius', 'Prius'), ('Land Cruiser', 'Land Cruiser'),
        ('Avensis', 'Avensis'), ('Camry', 'Camry'), ('Highlander', 'Highlander'), ('RAV4', 'RAV4'), ('Crown', 'Crown')
                )
     ),
    ('Renault', (('Latitude', 'Latitude'), ('Koleos', 'Koleos'), ('Arkana', 'Arkana'), ('Kaptur', 'Kaptur'), ('Fluence', 'Fluence'),
        ('Grand Scenic', 'Grand Scenic'), ('Laguna', 'Laguna'), ('Trafic', 'Trafic'), ('Logan Stepway', 'Logan Stepway'), ('Duster', 'Duster')
                )
     ),
    ('Opel', (('Insignia', 'Insignia'), ('Mokka', 'Mokka'), ('Astra GTC', 'Astra GTC'), ('Antara', 'Antara'), ('Astra Family', 'Astra Family'),
        ('Astra', 'Astra'), ('Zafira', 'Zafira'), ('Vivaro', 'Vivaro'), ('Corsa', 'Corsa'), ('Meriva', 'Meriva')
                )
     ),
    ('Honda', (('Legend', 'Legend'), ('Shuttle', 'Shuttle'), ('N-WGN', 'N-WGN'), ('Crosstour', 'Crosstour'), ('Civic Type R', 'Civic Type R'),
        ('Vezel', 'Vezel'), ('CR-Z', 'CR-Z'), ('Jade', 'Jade'), ('Fit Shuttle', 'Fit Shuttle'), ('Freed Spike', 'Freed Spike')
                )
     ),
    ('BMW', (('6-Series', '6-Series'), ('X6', 'X6'), ('X5', 'X5'), ('5-Series Gran Turismo', '5-Series Gran Turismo'), ('X4', 'X4'),
        ('X3', 'X3'), ('7-Series', '7-Series'), ('3-Series Gran Turismo', '3-Series Gran Turismo'), ('5-Series', '5-Series'), ('Z4', 'Z4')
                )
     )

]
class Services(models.Model):
    service_name = models.CharField('Название услуги', max_length=50, default='')
    service_price = models.DecimalField('Стоимость', decimal_places=2, max_digits=5, default=0.0)
    service_time = models.IntegerField('Примерное время', default=1, help_text='Время указано в минутах')
    def __str__(self):
        return self.service_name
    class Meta:

        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Article(models.Model):

    fio = models.CharField('ФИО', max_length=30, default='Рубец Алексей Сергеевич')
    car = models.CharField('Автомобиль', max_length=30, choices=CARS, default='Не указан')

    phone_number = models.CharField('Телефонный номер',
                                    validators=[RegexValidator(r'\+375(17|29|25|33|44)[0-9]{7}')],
                                    max_length=20,
                                    null=False,
                                    help_text="Телефонный номер должен быть в форме: '+375(17/25/29/33/44)XXXXXXX'.",
                                    blank=False)

    pub_order = models.DateTimeField('Дата заказа')
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)

    def __str__ (self):
        return self.fio
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
