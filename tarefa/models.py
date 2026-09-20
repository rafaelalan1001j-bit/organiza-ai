from django.db import models

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)

    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='tarefas')


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    