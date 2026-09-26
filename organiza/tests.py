from django.test import TestCase, Client
from django.urls import reverse
from .models import Tarefa, Categoria


class OrganizaSimplesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria, _ = Categoria.objects.get_or_create(nome="Estudos")
        self.tarefa = Tarefa.objects.create(
            titulo="Apresentar NAP2",
            descricao="Demonstrar o CRUD de tarefas e categorias",
            categoria=self.categoria,
            prioridade="alta"
        )

    def test_home_lista(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apresentar NAP2")

    def test_cadastrar_tarefa(self):
        dados = {
            'titulo': 'Estudar para Prova',
            'descricao': 'Capítulo 1 ao 4',
            'categoria': self.categoria.id,
            'prioridade': 'media'
        }
        response = self.client.post(reverse('home'), dados)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tarefa.objects.filter(titulo='Estudar para Prova').exists())

    def test_editar_tarefa(self):
        # GET
        response_get = self.client.get(reverse('editar_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Editar Tarefa")

        # POST
        dados = {
            'titulo': 'Apresentar NAP2 Atualizado',
            'categoria': self.categoria.id,
            'prioridade': 'alta'
        }
        response_post = self.client.post(reverse('editar_tarefa', args=[self.tarefa.id]), dados)
        self.assertEqual(response_post.status_code, 302)
        self.tarefa.refresh_from_db()
        self.assertEqual(self.tarefa.titulo, 'Apresentar NAP2 Atualizado')

    def test_concluir_tarefa(self):
        self.assertFalse(self.tarefa.concluida)
        response = self.client.post(reverse('concluir_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response.status_code, 302)
        self.tarefa.refresh_from_db()
        self.assertTrue(self.tarefa.concluida)

    def test_excluir_tarefa(self):
        response = self.client.post(reverse('excluir_tarefa', args=[self.tarefa.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tarefa.objects.filter(id=self.tarefa.id).exists())

    def test_crud_categoria(self):
        # Listar
        response = self.client.get(reverse('categorias'))
        self.assertEqual(response.status_code, 200)

        # Criar
        response = self.client.post(reverse('categorias'), {'nome': 'Trabalho Novo'})
        self.assertEqual(response.status_code, 302)
        nova_cat = Categoria.objects.get(nome='Trabalho Novo')

        # Excluir
        response = self.client.post(reverse('excluir_categoria', args=[nova_cat.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Categoria.objects.filter(id=nova_cat.id).exists())
