from django.db import models
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=130)
    email = models.CharField(max_length=150,unique=True)
    senha = models.CharField(max_length=8)
    #data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome


class Vaca(models.Model):
    usuario = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    nome = models.CharField(max_length=30,unique=True)
    raca = models.CharField(max_length=150)
    idade = models.IntegerField(max_length=8)
    kg = models.IntegerField(max_length=8)


    
    def __str__(self):
        return self.nome



class Rendimento(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE)
    litros = models.DecimalField(max_digits=10, decimal_places=3)
    dia = models.DateField()

    def __str__(self):
        return str(self.litros)



