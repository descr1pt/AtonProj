from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, default='Иванов')
    last_name = models.CharField(max_length=128, default='Иван')
    middle_name = models.CharField(max_length=128, default='Иванович')

    # для удобного отображения на странице администратора
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Client(models.Model):
    acc_num = models.CharField(max_length=128)
    fam = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    otc = models.CharField(max_length=128,)
    birth_date = models.DateField()
    inn = models.IntegerField()
    respons = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    STAT_CHOICES = (
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    )
    status = models.CharField(max_length=20, choices=STAT_CHOICES, default='Не в работе')

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'

