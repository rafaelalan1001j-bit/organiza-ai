from django.contrib import admin
from .models import Categoria, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'prioridade', 'data_limite', 'concluida', 'data_criacao')
    list_filter = ('concluida', 'prioridade', 'categoria', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    list_editable = ('concluida', 'prioridade')
    date_hierarchy = 'data_criacao'
