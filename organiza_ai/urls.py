from django.contrib import admin
from django.urls import path
from tarefa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='home_raiz'),
    path('menu/', views.menu),
    path('lista_tarefas/', views.lista_tarefas, name='lista_tarefas'),
]
