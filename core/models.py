from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, db_column='nome')
    importancia = models.CharField(max_length=25, null=True, blank=True)

def str (self):
    return self.nome
