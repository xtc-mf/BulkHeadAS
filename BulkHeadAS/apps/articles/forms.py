from django import forms
from django.forms import ModelForm
from .models import *

phone_regex = r'\+375(17|29|25|33|44)[0-9]{7}'
regex_error = 'Телефонный номер должен быть в формате: +375(17/25/29/33/44)1234567.'

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
     ),
    ('Mercedes-Benz', (('CLS-Class', 'CLS-Class'), ('GLA-Class', 'GLA-Class'), ('GL-Class', 'GL-Class'), ('GLE-Coupe', 'GLE-Coupe'), ('CL-Class', 'CL-Class'),
        ('GLE', 'GLE'), ('S-Class', 'S-Class'), ('GLK-CLASS', 'GLK-Class'), ('GLS-Class', 'GLS-Class'), ('CLK-Class', 'CLK-Class')
                )
     ),
    ('Audi', (('A7', 'A7'), ('Q7', 'Q7'), ('A5', 'A5'), ('Q5', 'Q5'), ('Q3', 'Q3'),
        ('A1', 'A1'), ('TT', 'TT'), ('A3', 'A3'), ('A8', 'A8'), ('A6 Allroad Quattro', 'A6 Allroad Quattro')
                )
     ),
    ('Geely', (('Coolray SX11', 'Coolray SX11'), ('Atlas', 'Atlas'), ('Emgrand EC7', 'Emgrand EC7'), ('Vision', 'Vision'), ('GC6', 'GC6'),
        ('MK Cross', 'MK Cross'), ('MK', 'MK'), ('Emgrand X7', 'Emgrand X7'), ('Otaka CK', 'Otaka CK'), ('CK', 'CK')
                )
     ),
    ('Lada', (('Granta Sport', 'Granta Sport'), ('Vesta Cross', 'Vesta Cross'), ('Vesta', 'Vesta'), ('Kalina Cross', 'Kalina Cross'), ('X-Ray Cross', 'X-Ray Cross'),
        ('Kalina Sport', 'Kalina Sport'), ('Granta Cross', 'Granta Cross'), ('X-Ray', 'X-Ray'), ('Largus', 'Largus'), ('Largus Cross', 'Largus Cross')
                )
     ),
    ('Volkswagen', (('Passat CC', 'Passat CC'), ('Touareg', 'Touareg'), ('Tiguan', 'Tiguan'), ('Phaeton', 'Phaeton'), ('Scirocco', 'Scirocco'),
        ('Amarok', 'Amarok'), ('Beetle', 'Beetle'), ('Jetta', 'Jetta'), ('Multivan', 'Multivan'), ('Touran', 'Touran')
                )
     ),
    ('Škoda', (('Superb', 'Superb'), ('Kodiaq', 'Kodiaq'), ('Rapid', 'Rapid'), ('Octavia', 'Octavia'), ('Karoq', 'Karoq'),
        ('Yeti', 'Yeti  '), ('Fabia', 'Fabia'), ('Roomster', 'Roomster'), ('Felicia', 'Felicia')
                )
     ),
    ('Nissan', (('Leaf', 'Leaf'), ('Teana', 'Teana'), ('Terrano', 'Terrano'), ('Cima', 'Cima'), ('Silvia', 'Silvia'),
        ('Almera', 'Almera'), ('Murrano', 'Murrano'), ('Patrol', 'Patrol'), ('Sentra', 'Sentra'), ('X-Trail', 'X-Trail')
                )
     ),
]

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class Entrollment(ModelForm):

    fio = forms.CharField(label="Фамилия Имя Отчество",
                           max_length=30,
                           validators=[(RegexValidator(r'[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][А-Яа-яЁёA-Za-z]{2,25}\s?'))],
                          )
    car = forms.ChoiceField(choices = CARS, label='Автомобиль')
    phone_number = forms.RegexField(regex=phone_regex,
                                    label='Номер телефона',
                                    help_text="Телефонный номер должен быть в формате: +375(17/25/29/33/44)XXXXXXX.",
                                    )
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    pub_order = forms.DateTimeField(label="Запись на", widget=DateInput)
    class Meta:
        model = Article
        widgets = { 'my_date_field': DateInput() }
        fields = ["fio", "car", "phone_number", "client_service", "pub_order"]
        labels = {'fio': 'ФИО', "car": "Автомобиль", "phone_number": "Телефонный номер", "client_service": "Услуга", "pub_order": "Время записи"}
