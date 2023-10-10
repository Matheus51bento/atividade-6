from django.db import models


class Selo(models.Model):
    texto = models.CharField(max_length=80)

    def __str__(self):
        return self.texto


class Disco(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    selo_fonografico = models.ForeignKey(Selo, null=True, blank=True, on_delete=models.CASCADE)
    ano = models.IntegerField()
    pais = models.CharField(max_length=80)
    genero = models.CharField(max_length=80)
    quantidade = models.BigIntegerField()

    def __str__(self):
        return self.nome

class Artista(models.Model):
    nome = models.CharField(max_length=80)
    discos = models.ManyToManyField(Disco)

    def __str__(self):
        return self.nome
