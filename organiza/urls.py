from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('tarefa/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefa/<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:pk>/excluir/', views.excluir_categoria, name='excluir_categoria'),
]
