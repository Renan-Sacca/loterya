from django.db import models
from django.contrib.auth.models import User
from Home.models import fichas

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    senha = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)
    sexo =  models.CharField(max_length=50)
    cod_conf = models.IntegerField()
    ativado = models.BooleanField()
