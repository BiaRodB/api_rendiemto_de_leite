from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=130)
    email = models.CharField(max_length=150,unique=True)
    senha = models.CharField(max_length=8)
    #data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome


class Vaca(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, unique=True)
    raca = models.CharField(max_length=150)
    idade = models.IntegerField()
    kg = models.FloatField()

    def __str__(self):
       return self.nome

class Rendimento(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE)
    litros = models.DecimalField(max_digits=10, decimal_places=3)
    dia = models.CharField(max_length=10)

    def __str__(self):
        return str(self.litros)



