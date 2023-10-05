from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    selo_fonografico = models.CharField(max_length=100)
    ano = models.IntegerField()
    pais = models.CharField(max_length=80)
    genero = models.CharField(max_length=80)
    quantidade = models.BigIntegerField()

    def __str__(self):
        return self.nome
