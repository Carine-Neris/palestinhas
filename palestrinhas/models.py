from tabnanny import verbose
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
                                choices=STATUS_CHOICES,
                                default='Já Vi')
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Palestras"