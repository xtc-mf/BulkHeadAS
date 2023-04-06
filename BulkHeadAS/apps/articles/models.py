from django.core.validators import RegexValidator
from django.db import models
"""
CARS = [
    ('Toyota',
     (('C-HR', 'C-HR'), ('Sai', 'Sai'), ('Auris', 'Auris'), ('Prius', 'Prius'), ('Land Cruiser', 'Land Cruiser'),
      ('Avensis', 'Avensis'), ('Camry', 'Camry'), ('Highlander', 'Highlander'), ('RAV4', 'RAV4'), ('Crown', 'Crown')
      )
     ),
    ('Renault', (
    ('Latitude', 'Latitude'), ('Koleos', 'Koleos'), ('Arkana', 'Arkana'), ('Kaptur', 'Kaptur'), ('Fluence', 'Fluence'),
    ('Grand Scenic', 'Grand Scenic'), ('Laguna', 'Laguna'), ('Trafic', 'Trafic'), ('Logan Stepway', 'Logan Stepway'),
    ('Duster', 'Duster')
    )
     ),
    ('Opel', (('Insignia', 'Insignia'), ('Mokka', 'Mokka'), ('Astra GTC', 'Astra GTC'), ('Antara', 'Antara'),
              ('Astra Family', 'Astra Family'),
              ('Astra', 'Astra'), ('Zafira', 'Zafira'), ('Vivaro', 'Vivaro'), ('Corsa', 'Corsa'), ('Meriva', 'Meriva')
              )
     ),
    ('Honda', (('Legend', 'Legend'), ('Shuttle', 'Shuttle'), ('N-WGN', 'N-WGN'), ('Crosstour', 'Crosstour'),
               ('Civic Type R', 'Civic Type R'),
               ('Vezel', 'Vezel'), ('CR-Z', 'CR-Z'), ('Jade', 'Jade'), ('Fit Shuttle', 'Fit Shuttle'),
               ('Freed Spike', 'Freed Spike')
               )
     ),
    ('BMW', (('6-Series', '6-Series'), ('X6', 'X6'), ('X5', 'X5'), ('5-Series Gran Turismo', '5-Series Gran Turismo'),
             ('X4', 'X4'),
             ('X3', 'X3'), ('7-Series', '7-Series'), ('3-Series Gran Turismo', '3-Series Gran Turismo'),
             ('5-Series', '5-Series'), ('Z4', 'Z4')
             )
     ),
    ('Mercedes-Benz', (
    ('CLS-Class', 'CLS-Class'), ('GLA-Class', 'GLA-Class'), ('GL-Class', 'GL-Class'), ('GLE-Coupe', 'GLE-Coupe'),
    ('CL-Class', 'CL-Class'),
    ('GLE', 'GLE'), ('S-Class', 'S-Class'), ('GLK-CLASS', 'GLK-Class'), ('GLS-Class', 'GLS-Class'),
    ('CLK-Class', 'CLK-Class')
    )
     ),
    ('Audi', (('A7', 'A7'), ('Q7', 'Q7'), ('A5', 'A5'), ('Q5', 'Q5'), ('Q3', 'Q3'),
              ('A1', 'A1'), ('TT', 'TT'), ('A3', 'A3'), ('A8', 'A8'), ('A6 Allroad Quattro', 'A6 Allroad Quattro')
              )
     ),
    ('Geely', (
    ('Coolray SX11', 'Coolray SX11'), ('Atlas', 'Atlas'), ('Emgrand EC7', 'Emgrand EC7'), ('Vision', 'Vision'),
    ('GC6', 'GC6'),
    ('MK Cross', 'MK Cross'), ('MK', 'MK'), ('Emgrand X7', 'Emgrand X7'), ('Otaka CK', 'Otaka CK'), ('CK', 'CK')
    )
     ),
    ('Lada', (('Granta Sport', 'Granta Sport'), ('Vesta Cross', 'Vesta Cross'), ('Vesta', 'Vesta'),
              ('Kalina Cross', 'Kalina Cross'), ('X-Ray Cross', 'X-Ray Cross'),
              ('Kalina Sport', 'Kalina Sport'), ('Granta Cross', 'Granta Cross'), ('X-Ray', 'X-Ray'),
              ('Largus', 'Largus'), ('Largus Cross', 'Largus Cross')
              )
     ),
    ('Volkswagen', (('Passat CC', 'Passat CC'), ('Touareg', 'Touareg'), ('Tiguan', 'Tiguan'), ('Phaeton', 'Phaeton'),
                    ('Scirocco', 'Scirocco'),
                    ('Amarok', 'Amarok'), ('Beetle', 'Beetle'), ('Jetta', 'Jetta'), ('Multivan', 'Multivan'),
                    ('Touran', 'Touran')
                    )
     ),
    ('Lexus', (('LX570', 'LX570'), ('GS350', 'GS350'), ('IS250', 'RX450h'), ('ES250', 'ES250'), ('GS250', 'GS250'),
               ('LS430', 'LS430'), ('LS600hL', 'LS600hl'), ('NX200t', 'NX200t'), ('RX400h', 'RX400h'),
               ('RX350', 'RX350')
               )
     ),
    ('Škoda',
     (('Superb', 'Superb'), ('Kodiaq', 'Kodiaq'), ('Rapid', 'Rapid'), ('Octavia', 'Octavia'), ('Karoq', 'Karoq'),
      ('Yeti', 'Yeti  '), ('Fabia', 'Fabia'), ('Roomster', 'Roomster'), ('Felicia', 'Felicia')
      )
     ),
    ('Nissan', (('Leaf', 'Leaf'), ('Teana', 'Teana'), ('Terrano', 'Terrano'), ('Cima', 'Cima'), ('Silvia', 'Silvia'),
                ('Almera', 'Almera'), ('Murrano', 'Murrano'), ('Patrol', 'Patrol'), ('Sentra', 'Sentra'),
                ('X-Trail', 'X-Trail')
                )
     ),
    ('Citroën', (
    ('C-Crosser', 'C-Crosser'), ('DS4', 'DS4'), ('C5', 'C5'), ('C4 Aircross', 'C4 Aircross'), ('C-Elysee', 'C-Elysee'),
    ('C1', 'C1'), ('DS5', 'DS5'), ('C4 Picasso', 'C4 Picasso'), ('C4 Grand Picasso', 'C4 Grand Picasso'), ('C3', 'C3')
    )
     ),
    ('Peugeot', (('208', '208'), ('508', '508'), ('3008', '3008'), ('4007', '4007'), ('4008', '4008'),
                 ('408', '408'), ('407', '407'), ('607', '607'), ('Expert', 'Expert'), ('2008', '2008')
                 )
     ),
    ('Mitshubishi', (
    ('Lancer Evolution', 'Lancer Evolution'), ('Grandis', 'Grandis'), ('Eclipse Cross', 'Eclipse Cross'),
    ('GTO', 'GTO'), ('Outlander', 'Outlander'),
    ('Delica D5', 'Delica D5'), ('FTO', 'FTO'), ('Galant', 'Galant'), ('ASX', 'ASX'), ('Pajero', 'Pajero')
    )
     ),
    ('KIA', (('Optima', 'Optima'), ('K5', 'K5'), ('Quoris', 'Quoris'), ('Stinger', 'Stinger'), ('Rio', 'Rio'),
             ('Rio X', 'Rio X'), ('Operus', 'Operus'), ('Sportage', 'Sportage'), ('Soul', 'Soul'), ('Mohave', 'Mohave')
             )
     )

]
"""
class Services(models.Model):
    service_name = models.CharField('Название услуги', max_length=50, default='')
    service_price = models.DecimalField('Стоимость', decimal_places=2, max_digits=5, default=0.0)
    service_time = models.IntegerField('Примерное время', default=1, help_text='Время указано в минутах')

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
class Car(models.Model):
    name = models.CharField('Марка', max_length=25, default='None')
    model = models.CharField('Модель', max_length=25, default='None')

    def __str__(self):
        return self.name + " " + self.model

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Client(models.Model):
    fio = models.CharField('ФИО',
                           max_length=50,
                           validators=[(RegexValidator(
                               r'[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][А-Яа-яЁёA-Za-z]{2,25}\s?'))],
                           default='Рубец Алексей Сергеевич')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=1)
    #car = models.ForeignKey(Car, on_delete=models.CASCADE, default=0)

    phone_number = models.CharField('Телефонный номер',
                                    validators=[RegexValidator(r'\+375(17|29|25|33|44)[0-9]{7}')],
                                    max_length=20,
                                    null=False,
                                    help_text="Телефонный номер должен быть в форме: '+375(17/25/29/33/44)XXXXXXX'.",
                                    blank=False)

    pub_order = models.DateTimeField('Дата заказа')
    client_service = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Employee(models.Model):
    employee_fio = models.CharField('ФИО',
                                    max_length=50,
                                    validators=[(RegexValidator(
                                        r'[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][А-Яа-яЁёA-Za-z]{2,25}\s?'))],
                                    default='Рубец Алексей Сергеевич')
    employee_age = models.IntegerField('Возраст', default=18, help_text='Возраст работника')
    employee_phoneNumber = models.CharField('Телефонный номер',
                                            validators=[RegexValidator(r'\+375(17|29|25|33|44)[0-9]{7}')],
                                            max_length=20,
                                            null=False,
                                            help_text="Телефонный номер должен быть в форме: '+375(17/25/29/33/44)XXXXXXX'.",
                                            blank=False)
    employee_rank = models.CharField('Должность',
                                     max_length=25,
                                     default='')
    employee_client = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.employee_fio) + " " + str(self.employee_rank)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class Work(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=0)
    is_done = models.BooleanField('Работа выполнена', default=False)

    def __str__(self):
        if self.is_done == True:
            return str(self.employee) + " выполнил заказ " + str(self.client)
        else:
            return str(self.employee) + " работает с заказом " + str(self.client)

    class Meta:
        verbose_name = 'Текущая работа'
        verbose_name_plural = 'Текущие работы'