from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Categoria


def home(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        categoria_id = request.POST.get('categoria')
        prioridade = request.POST.get('prioridade', 'media')
        data_limite = request.POST.get('data_limite') or None

        if titulo:
            categoria = Categoria.objects.filter(id=categoria_id).first() if categoria_id else None
            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao if descricao else None,
                categoria=categoria,
                prioridade=prioridade,
                data_limite=data_limite
            )
        return redirect('home')

    status_filtro = request.GET.get('status', 'todas')
    categoria_filtro = request.GET.get('categoria', '')
    busca = request.GET.get('q', '').strip()

    tarefas = Tarefa.objects.select_related('categoria').all()

    if status_filtro == 'pendentes':
        tarefas = tarefas.filter(concluida=False)
    elif status_filtro == 'concluidas':
        tarefas = tarefas.filter(concluida=True)

    if categoria_filtro:
        tarefas = tarefas.filter(categoria_id=categoria_filtro)

    if busca:
        tarefas = tarefas.filter(titulo__icontains=busca)

    total = Tarefa.objects.count()
    pendentes = Tarefa.objects.filter(concluida=False).count()
    concluidas = Tarefa.objects.filter(concluida=True).count()
    categorias = Categoria.objects.all()

    return render(request, 'lista.html', {
        'tarefas': tarefas,
        'categorias': categorias,
        'status_filtro': status_filtro,
        'categoria_filtro': categoria_filtro,
        'busca': busca,
        'total': total,
        'pendentes': pendentes,
        'concluidas': concluidas,
    })


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        categoria_id = request.POST.get('categoria')
        prioridade = request.POST.get('prioridade', 'media')
        data_limite = request.POST.get('data_limite') or None

        if titulo:
            tarefa.titulo = titulo
            tarefa.descricao = descricao if descricao else None
            tarefa.categoria = Categoria.objects.filter(id=categoria_id).first() if categoria_id else None
            tarefa.prioridade = prioridade
            tarefa.data_limite = data_limite
            tarefa.save()
            return redirect('home')

    categorias = Categoria.objects.all()
    return render(request, 'editar.html', {
        'tarefa': tarefa,
        'categorias': categorias
    })


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('home')


def concluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('home')


def categorias(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        if nome and not Categoria.objects.filter(nome__iexact=nome).exists():
            Categoria.objects.create(nome=nome)
            return redirect('categorias')

    lista = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': lista})


def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('categorias')
