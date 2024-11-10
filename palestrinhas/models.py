from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('Já Vi', 'Já Vi'),
    ('Quero Ver', 'Quero Ver')
]


class Palestras(models.Model):
    nome = models.CharField(max_length=150)
    link = models.URLField()
    descricao = models.CharField(max_length=400)
    data_criacao = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='Já Vi')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Palestras"


class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    palestra = models.ForeignKey(Palestras, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.user} na palestra {self.palestra}"
