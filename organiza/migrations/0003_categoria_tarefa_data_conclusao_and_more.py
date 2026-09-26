import django.db.models.deletion
from django.db import migrations, models


def seed_and_clean_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Categoria = apps.get_model('organiza', 'Categoria')
    cat_dados = [
        ('Estudos', '#8b5cf6', 'bi-book', 'Atividades acadêmicas, cursos e leituras'),
        ('Trabalho', '#3b82f6', 'bi-briefcase', 'Demandas profissionais, relatórios e reuniões'),
        ('Produtividade', '#10b981', 'bi-check2-circle', 'Metas semanais, hábitos e organização pessoal'),
        ('Pessoal', '#f59e0b', 'bi-person', 'Compromissos pessoais, saúde e lazer'),
        ('Projetos', '#06b6d4', 'bi-kanban', 'Desenvolvimento de projetos e entregas acadêmicas'),
        ('Geral', '#64748b', 'bi-folder', 'Tarefas gerais do dia a dia'),
    ]
    for nome, cor, icone, desc in cat_dados:
        Categoria.objects.using(db_alias).get_or_create(
            nome=nome,
            defaults={'cor': cor, 'icone': icone, 'descricao': desc}
        )


def link_tarefas_categorias(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Categoria = apps.get_model('organiza', 'Categoria')
    Tarefa = apps.get_model('organiza', 'Tarefa')
    Subtarefa = apps.get_model('organiza', 'Subtarefa')

    cat_estudos = Categoria.objects.using(db_alias).filter(nome='Estudos').first()
    cat_trabalho = Categoria.objects.using(db_alias).filter(nome='Trabalho').first()
    cat_prod = Categoria.objects.using(db_alias).filter(nome='Produtividade').first()
    cat_geral = Categoria.objects.using(db_alias).filter(nome='Geral').first()

    for t in Tarefa.objects.using(db_alias).all():
        titulo_lower = t.titulo.lower()
        if 'estudo' in titulo_lower or 'django' in titulo_lower or 'livro' in titulo_lower:
            t.categoria = cat_estudos
        elif 'apresenta' in titulo_lower or 'trabalho' in titulo_lower or 'projeto' in titulo_lower:
            t.categoria = cat_trabalho
        elif 'organizar' in titulo_lower or 'semana' in titulo_lower:
            t.categoria = cat_prod
        else:
            t.categoria = cat_geral or cat_prod
        t.save(using=db_alias)

        if t.subtarefas.using(db_alias).count() == 0:
            if 'django' in titulo_lower:
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Revisar Models e Migrations', concluida=True)
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Construir Views e Forms', concluida=True)
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Implementar Templates e Bootstrap 5', concluida=False)
            elif 'apresenta' in titulo_lower:
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Definir tópicos dos slides', concluida=True)
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Gravar vídeo ou roteiro de demonstração', concluida=True)
            elif 'organizar' in titulo_lower:
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Planejar rotina de segunda a sexta', concluida=True)
                Subtarefa.objects.using(db_alias).create(tarefa=t, titulo='Definir metas de produtividade', concluida=True)


class Migration(migrations.Migration):

    dependencies = [
        ('organiza', '0002_alter_tarefa_options_remove_tarefa_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')),
                ('cor', models.CharField(default='#6366f1', max_length=20, verbose_name='Cor de Destaque')),
                ('icone', models.CharField(default='bi-folder', max_length=50, verbose_name='Ícone')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.RunPython(seed_and_clean_data, reverse_code=migrations.RunPython.noop),
        migrations.RunSQL(
            "UPDATE organiza_tarefa SET categoria = (SELECT id FROM organiza_categoria WHERE nome='Geral' LIMIT 1);",
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.AddField(
            model_name='tarefa',
            name='data_conclusao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Conclusão'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_limite',
            field=models.DateField(blank=True, null=True, verbose_name='Data Limite / Prazo'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarefas', to='organiza.categoria', verbose_name='Categoria'),
        ),
        migrations.CreateModel(
            name='Subtarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título da Subtarefa')),
                ('concluida', models.BooleanField(default=False, verbose_name='Concluída')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtarefas', to='organiza.tarefa', verbose_name='Tarefa Principal')),
            ],
            options={
                'verbose_name': 'Subtarefa',
                'verbose_name_plural': 'Subtarefas',
                'ordering': ['concluida', 'data_criacao'],
            },
        ),
        migrations.RunPython(link_tarefas_categorias, reverse_code=migrations.RunPython.noop),
    ]

