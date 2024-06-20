from django.urls import path
from fichas.views import ListarFichas, CriarFichas, EditarFichas, DeletarFichas #FotoFicha
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListarFichas.as_view(), name='listar-fichas'),
    path('novo/', CriarFichas.as_view(), name = 'criar-fichas'),
    path('<int:pk>/', EditarFichas.as_view(), name = 'editar-fichas'),
    path('deletar/<int:pk>', DeletarFichas.as_view(), name = 'deletar-fichas'),
    #path('fotos/<str:arquivo>/', FotoFicha.as_view(), name='foto-ficha'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)