from django.db import models


STATUS_CHOICES = [
    ('Já Vi', 'Já Vi'),
    ('Quero Ver', 'Quero Ver')
]


class Palestras(models.Model):
    nome = models.CharField(max_length=150)
    link = models.URLField()
    descricao = models.CharField(max_length=400)
    data_criacao = models.DateField()
    status = models.CharField(max_length = 10,
                                choices=STATUS_CHOICES,
                                default='Já Vi')
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Palestras"