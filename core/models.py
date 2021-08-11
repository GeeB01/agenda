from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    # Criação da classe meta para alterar o nome da table padrao de core_evento para Evento
    class Meta:
        db_table = 'evento'
    # Fim da classe Meta

    def __str__(self):
        return self.titulo
