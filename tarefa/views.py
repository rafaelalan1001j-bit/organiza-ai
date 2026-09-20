from django.shortcuts import render

# Create your views here.
def menu(request):   
    return render(request, 'tarefa/menu.html')

def lista_tarefas(request):
    return render(request, 'tarefa/lista_tarefas.html')
