from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item
from .consts import OPCOES_RARIDADE
from .forms import FormularioItem

class ItemModelTests(TestCase):
    def setUp(self):
        # Criando um item de exemplo para usar nos testes
        self.item = Item.objects.create(
            nome='Espada Lendária',
            descricao='Uma espada forjada por anões.',
            durabilidade=100,
            raridade=1,
            foto=None
        )

    def test_get_nome_raridade(self):
        # Testando o método get_nome_raridade
        nome_raridade = self.item.get_nome_raridade()
        expected_raridade = dict(OPCOES_RARIDADE).get(1)
        self.assertEqual(nome_raridade, expected_raridade)

    def test_create_item(self):
        # Testando a criação de um item
        item = Item.objects.create(
            nome='Escudo Mágico',
            descricao='Um escudo encantado com runas antigas.',
            durabilidade=150,
            raridade=2, 
            foto=None
        )
        self.assertEqual(item.nome, 'Escudo Mágico')
        self.assertEqual(item.descricao, 'Um escudo encantado com runas antigas.')
        self.assertEqual(item.durabilidade, 150)
        self.assertEqual(item.raridade, 2)

    def test_get_raridade_display(self):
        # Testando o método get_raridade_display
        raridade_display = self.item.get_raridade_display()
        expected_raridade = dict(OPCOES_RARIDADE).get(1)
        self.assertEqual(raridade_display, expected_raridade)

class ListarItensTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('listar-itens')
        Item.objects.create(nome='Espada Lendária', descricao='Uma espada forjada por anões.', durabilidade=100, raridade=1)
        Item.objects.create(nome='Escudo Mágico', descricao='Um escudo encantado com runas antigas.', durabilidade=150, raridade=2)

    def test_listar_itens_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/listar.html')
        self.assertContains(response, 'Espada Lendária')
        self.assertContains(response, 'Escudo Mágico')

class CriarItensTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('criar-itens')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_criar_itens_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/novo.html')

    def test_criar_itens_post(self):
        data = {
            'nome': 'Novo Item',
            'descricao': 'Descrição do novo item.',
            'durabilidade': 100,
            'raridade': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Item.objects.filter(nome='Novo Item').exists())

class EditarItensTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = Item.objects.create(nome='Espada Lendária', descricao='Uma espada forjada por anões.', durabilidade=100, raridade=1)
        self.url = reverse('editar-itens', args=[self.item.id])
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_editar_itens_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/editar.html')

    def test_editar_itens_post(self):
        data = {
            'nome': 'Espada Atualizada',
            'descricao': 'Descrição atualizada.',
            'durabilidade': 200,
            'raridade': 2
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.nome, 'Espada Atualizada')
        self.assertEqual(self.item.durabilidade, 200)

class DeletarItensTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.item = Item.objects.create(nome='Espada Lendária', descricao='Uma espada forjada por anões.', durabilidade=100, raridade=1)
        self.url = reverse('deletar-itens', args=[self.item.id])
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_deletar_itens_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/deletar.html')

    def test_deletar_itens_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())

class FormularioItemTests(TestCase):

    def test_formulario_item_valido(self):
        data = {
            'nome': 'Espada Lendária',
            'descricao': 'Uma espada forjada por anões.',
            'durabilidade': 100,
            'raridade': 1
        }
        form = FormularioItem(data=data)
        self.assertTrue(form.is_valid())

    def test_formulario_item_nome_vazio(self):
        data = {
            'nome': '',
            'descricao': 'Uma espada forjada por anões.',
            'durabilidade': 100,
            'raridade': 1
        }
        form = FormularioItem(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_formulario_item_raridade_invalida(self):
        data = {
            'nome': 'Espada Lendária',
            'descricao': 'Uma espada forjada por anões.',
            'durabilidade': 100,
            'raridade': 99  # Supondo que 99 não seja uma raridade válida
        }
        form = FormularioItem(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('raridade', form.errors)