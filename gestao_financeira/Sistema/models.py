from django.db import models
from django.contrib.auth.models import User

class CustoFixo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='custos_fixos')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class Despesa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='despesas')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class Investimento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
