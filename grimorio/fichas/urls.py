from django.urls import path
from fichas.views import ListarFichas, FotoFicha, CriarFichas, EditarFichas, DeletarFichas

urlpatterns = [
    path('', ListarFichas.as_view(), name='listar-fichas'),
    path('novo/', CriarFichas.as_view(), name = 'criar-fichas'),
    path('<int:pk>/', EditarFichas.as_view(), name = 'editar-fichas'),
    path('deletar/<int:pk>', DeletarFichas.as_view(), name = 'deletar-fichas'),
    path('fotos/<str:arquivo>/', FotoFicha.as_view(), name='foto-ficha')
]