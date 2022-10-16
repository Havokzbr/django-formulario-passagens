from django.db import models
from .classe_viagem import ClasseViagem


class Passagem(models.Model):
    data_pesquisa = models.DateField()
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    qtd_adultos = models.IntegerField()
    qtd_criancas = models.IntegerField()
    classes_viagem = models.CharField(max_length=4, choices=ClasseViagem.choices, default=0)
    informacoes = models.TextField(max_length=200, blank=True)

