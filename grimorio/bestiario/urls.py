from django.urls import path
from bestiario.views import ListarCriaturas, CriarCriaturas, EditarCriaturas, DeletarCriaturas 

urlpatterns = [
    path('', ListarCriaturas.as_view(), name='listar-criaturas'),
    path('novo/', CriarCriaturas.as_view(), name = 'criar-criaturas'),
    path('<int:pk>/', EditarCriaturas.as_view(), name = 'editar-criaturas'),
    path('deletar/<int:pk>', DeletarCriaturas.as_view(), name = 'deletar-criaturas'),
]