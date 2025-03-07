from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    imagem = models.ImageField(upload_to='static/img/media/receitas', blank=True, null=True)

    def __str__(self):
        return self.nome_receita

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='media/perfis/', default='media/perfis/default.jpg')

    def __str__(self):
        return self.user.username

