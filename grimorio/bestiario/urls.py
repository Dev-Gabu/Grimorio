from django.urls import path, include
from bestiario.views import ListarCriaturas, CriarCriaturas, EditarCriaturas, DeletarCriaturas, DetalhesCriaturas, CriaturasAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'criaturas', CriaturasAPI)

urlpatterns = [
    path('', ListarCriaturas.as_view(), name='listar-criaturas'),
    path('novo/', CriarCriaturas.as_view(), name = 'criar-criaturas'),
    path('<int:pk>/', DetalhesCriaturas.as_view(), name = 'detalhes-criaturas'),
    path('editar/<int:pk>/', EditarCriaturas.as_view(), name = 'editar-criaturas'),
    path('deletar/<int:pk>', DeletarCriaturas.as_view(), name = 'deletar-criaturas'),
    path('api/', include(router.urls)),
]