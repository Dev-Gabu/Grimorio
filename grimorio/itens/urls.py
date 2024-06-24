from django.urls import path
from itens.views import ListarItens,  CriarItens, EditarItens, DeletarItens 

urlpatterns = [
    path('', ListarItens.as_view(), name='listar-itens'),
    path('novo/', CriarItens.as_view(), name = 'criar-itens'),
    path('<int:pk>/', EditarItens.as_view(), name = 'editar-itens'),
    path('deletar/<int:pk>', DeletarItens.as_view(), name = 'deletar-itens'),
]