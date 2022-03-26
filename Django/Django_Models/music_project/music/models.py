from django.db import models

# Create your models here.

class Musico(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(decimal_places=2,max_digits=50000)
    altura = models.DecimalField(decimal_places=2,max_digits=3)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

    
class EstiloMusical(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    integrantes = models.ManyToManyField(Musico)
    custo_show = models.DecimalField(decimal_places=2,max_digits=100000) 
    estilo = models.ManyToManyField(EstiloMusical)
    def __str__(self) -> str:
        return self.nome