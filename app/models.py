from django.conf import settings
from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    senha = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'USUÁRIO'

class Equipamento(models.Model):
    tipo = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=50, null=False)
    valorLocacaoEquipamento = models.FloatField(null=False)
    fotoEquipamento = models.ImageField()
    horaDeUso = models.IntegerField(null=False)

    def __str__(self):
        return self.tipo


    class Meta:
        verbose_name = u'Equipamento'
        verbose_name_plural = u'EQUIPAMENTO'


class Estudio(models.Model):
    tamanho = models.CharField(max_length=50, null=False)
    valorLocacaoEstudio = models.FloatField(null=False)
    fotoEstudio = models.ImageField()
    horaDeUso = models.IntegerField(null=False)

    

    def __str__(self):
        return self.tamanho


    class Meta:
        verbose_name = u'Estúdio'
        verbose_name_plural = u'ESTÚDIO'


class Pedido(models.Model):

    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    equipamento = models.ForeignKey('Equipamento', on_delete=models.CASCADE)
    estudio = models.ForeignKey('Estudio', on_delete=models.CASCADE)
    nota_fiscal = models.CharField(max_length=100)
    data = models.DateField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.valor_pedido

    class Meta:
        verbose_name = u'Pedido'
        verbose_name_plural = u'PEDIDO'
     

