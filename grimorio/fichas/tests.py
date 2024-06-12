from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from fichas.models import Ficha
from fichas.forms import FormularioFicha
from fichas.consts import OPCOES_SISTEMA
from django.urls import reverse
from django.contrib.auth.models import User

class FichaModelTest(TestCase):

    def setUp(self):
        # Configurando opções de sistema para o teste
        self.sistema_dd = OPCOES_SISTEMA[0][0]  # Primeiro sistema na lista de opções
        self.sistema_tormenta = OPCOES_SISTEMA[1][0]  # Segundo sistema na lista de opções
        
        # Arquivo de imagem de exemplo
        self.foto_exemplo = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x00\x01\x02\x03',
            content_type='image/jpeg'
        )

    def test_criacao_ficha(self):
        ficha = Ficha.objects.create(
            nome="Aragorn",
            sistema=self.sistema_dd,
            foto=self.foto_exemplo
        )
        self.assertEqual(ficha.nome, "Aragorn")
        self.assertEqual(ficha.sistema, self.sistema_dd)
        self.assertEqual(ficha.foto.name, 'fichas/fotos/test_image.jpg')

    def test_str_method(self):
        ficha = Ficha.objects.create(
            nome="Legolas",
            sistema=self.sistema_tormenta
        )
        expected_str = "Legolas - {}".format(dict(OPCOES_SISTEMA).get(self.sistema_tormenta))
        self.assertEqual(str(ficha), expected_str)

    def test_get_nome_sistema(self):
        ficha = Ficha.objects.create(
            nome="Gimli",
            sistema=self.sistema_dd
        )
        expected_nome_sistema = dict(OPCOES_SISTEMA).get(self.sistema_dd)
        self.assertEqual(ficha.get_nome_sistema(), expected_nome_sistema)

class FichaViewsTest(TestCase):

    def setUp(self):
        # Configurando opções de sistema para o teste
        self.sistema_dd = OPCOES_SISTEMA[0][0]
        self.sistema_tormenta = OPCOES_SISTEMA[1][0]

        # Criando usuário para teste de views que necessitam de autenticação
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Arquivo de imagem de exemplo
        self.foto_exemplo = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x00\x01\x02\x03',
            content_type='image/jpeg'
        )

        # Criando uma ficha de exemplo
        self.ficha = Ficha.objects.create(
            nome="Aragorn",
            sistema=self.sistema_dd,
            foto=self.foto_exemplo
        )

    def test_listar_fichas_view(self):
        response = self.client.get(reverse('listar-fichas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ficha/listar.html')
        self.assertContains(response, self.ficha.nome)

    def test_foto_ficha_view(self):
        response = self.client.get(reverse('foto-ficha', args=[self.ficha.foto.name.split('/')[-1]]))
        self.assertEqual(response.status_code, 200)

    def test_criar_ficha_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('criar-fichas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ficha/novo.html')

    def test_criar_ficha_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('criar-fichas'), {
            'nome': 'Legolas',
            'sistema': self.sistema_tormenta,
            'foto': self.foto_exemplo
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ficha.objects.filter(nome='Legolas').exists())

    def test_editar_ficha_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('editar-fichas', args=[self.ficha.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ficha/editar.html')

    def test_editar_ficha_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('editar-fichas', args=[self.ficha.id]), {
            'nome': 'Gimli',
            'sistema': self.sistema_dd
        })
        self.assertEqual(response.status_code, 302)
        self.ficha.refresh_from_db()
        self.assertEqual(self.ficha.nome, 'Gimli')

    def test_deletar_ficha_view_get(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('deletar-fichas', args=[self.ficha.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ficha/deletar.html')

    def test_deletar_ficha_view_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('deletar-fichas', args=[self.ficha.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Ficha.objects.filter(id=self.ficha.id).exists())