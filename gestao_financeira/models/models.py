from django.db import models
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    def clean(self):
        if not self.nome or not self.login or not self.senha:
            raise ValidationError("Todos os campos de usuário são obrigatórios.")

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    patrimonio_liquido = models.DecimalField(max_digits=15, decimal_places=2)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dividas = models.DecimalField(max_digits=15, decimal_places=2)
    metas = models.TextField()
    perfil = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='perfil_images/', null=True, blank=True)


class CustoFixo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)

class TipoDespesa(models.Model):
    descricao = models.CharField(max_length=100)

class DespesasExtras(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

class Investimentos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    valor_investido = models.DecimalField(max_digits=15, decimal_places=2)
    rentabilidade = models.DecimalField(max_digits=5, decimal_places=2)
    investimentos_fisicos = models.TextField()

class Relatorio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    conteudo = models.TextField()

