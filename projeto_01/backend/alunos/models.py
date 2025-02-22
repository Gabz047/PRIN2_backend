from django.db import models

# Create your models here.

class Estado(models.Model):

    nome = models.CharField(max_length=50)
    sigla= models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.sigla}"
    

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def  __str__(self):
        return self.nome