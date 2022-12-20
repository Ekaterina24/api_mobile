import datetime
from django.db import models

class Agent(models.Model):
    surname = models.CharField(verbose_name="Фамилия риелтора", max_length=100)
    name = models.CharField(verbose_name="Имя риелтора", max_length=100)
    patronymic = models.CharField(verbose_name="Отчество риелтора", max_length=100)
    share = models.IntegerField(verbose_name="Доля от комиссии")

    def __str__(self):
        return f'{self.surname}'

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + datetime.timedelta(days=1)  

class Event(models.Model):
    TYPE_CHOICES = [
        ('MEETING', 'Meeting'),
        ('PRESENTATION', 'Presentation'),
        ('PHONE_CALL', 'Phone_call'),
    ]

    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)

    datetime = models.TimeField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=12)
    duration = models.DurationField()
    comment = models.CharField(verbose_name="Комментарий", max_length=200)

    def __str__(self):
        return f'{self.comment}'


