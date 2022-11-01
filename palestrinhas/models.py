from email.policy import default
from pyexpat import model
from secrets import choice
from statistics import mode
from django.db import models


STATUS_CHOICES = [
    ('JV', 'Já Vi'),
    ('QV', 'Quero Ver')
]


class Palestras(models.Model):
    nome = models.CharField(max_length=150)
    link = models.URLField()
    descricao = models.CharField(max_length=400)
    data_criacao = models.DateField()
    status = models.CharField(max_length = 2,
                                choice=STATUS_CHOICES,
                                default='Já Vi')