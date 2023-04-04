from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, db_column='nome')

def str (self):
    return self.nome
