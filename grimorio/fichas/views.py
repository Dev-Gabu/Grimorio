from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from fichas.models import Ficha
from fichas.forms import FormularioFicha
from django.urls import reverse_lazy

class ListarFichas(ListView):

    model = Ficha
    context_object_name = 'fichas'
    template_name = 'fichas/listar.html'

    def get_queryset(self, **kwargs):
        queryset =  Ficha.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            query = queryset.filter(modelo_icontains=pesquisa)
        return queryset
    
# class FotoFicha(View):

#     def get(self, request, arquivo):
#         try:
#             #ficha = Ficha.objects.get(foto='fichas/fotos/{}'.format(arquivo))
#             fichas = Ficha.objects.get(foto='fichas/fotos/Mirio_-_Humano.jpg')
#             return FileResponse(fichas.foto)
#         except ObjectDoesNotExist:
#              raise Http404("Foto não encontrada ou arquivo não autorizado")
#         except Exception as exception:
#              raise exception
#         return 0

class CriarFichas(CreateView):

    model = Ficha
    form_class = FormularioFicha
    template_name = 'fichas/novo.html'
    success_url = reverse_lazy('listar-fichas')

class EditarFichas(UpdateView):
    model = Ficha
    form_class = FormularioFicha
    template_name = 'fichas/editar.html'
    success_url = reverse_lazy('listar-fichas')

class DeletarFichas(DeleteView):
    model = Ficha
    template_name = 'fichas/deletar.html'
    success_url = reverse_lazy('listar-fichas')