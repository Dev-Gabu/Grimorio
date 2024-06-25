from django.urls import path
from fichas.views import ListarFichas, CriarFichas, EditarFichas, DeletarFichas, DetalhesFichas

urlpatterns = [
    path('', ListarFichas.as_view(), name='listar-fichas'),
    path('novo/', CriarFichas.as_view(), name = 'criar-fichas'),
    path('<int:pk>/', DetalhesFichas.as_view(), name = 'detalhe-fichas'),
    path('editar/<int:pk>/', EditarFichas.as_view(), name = 'editar-fichas'),
    path('deletar/<int:pk>', DeletarFichas.as_view(), name = 'deletar-fichas'),
]