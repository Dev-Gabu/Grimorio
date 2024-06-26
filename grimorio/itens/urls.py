from django.urls import path, include
from itens.views import ListarItens,  CriarItens, EditarItens, DeletarItens, DetalhesItens, ItensAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItensAPI)

urlpatterns = [
    path('', ListarItens.as_view(), name='listar-itens'),
    path('novo/', CriarItens.as_view(), name = 'criar-itens'),
    path('<int:pk>/', DetalhesItens.as_view(), name = 'detalhes-itens'),
    path('editar/<int:pk>/', EditarItens.as_view(), name = 'editar-itens'),
    path('deletar/<int:pk>', DeletarItens.as_view(), name = 'deletar-itens'),
    path('api/', include(router.urls)),
]