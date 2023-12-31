from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Categoria (models.Model):
    chave = models.CharField(max_length=100, null=False, blank=False)
    valor = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.valor
    
ch=[]
categorias = Categoria.objects.order_by('valor')
for cat in categorias:
    ch.append((cat.chave, cat.valor))


class Fotografia (models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=ch, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.nome
    
