from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from itens.models import Item
from itens.forms import FormularioItem
from django.urls import reverse_lazy

class ListarItens(ListView):

    model = Item
    context_object_name = 'itens'
    template_name = 'item/listar.html'

    def get_queryset(self, **kwargs):
        queryset =  Item.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            query = queryset.filter(modelo_icontains=pesquisa)
        return queryset
    
# class FotoItem(View):

#     def get(self, request, arquivo):
#         try:
#             item = Item.objects.get(foto='item/fotos/{}'.format(arquivo))
#             return FileResponse(item.foto)
#         except ObjectDoesNotExist:
#              raise Http404("Foto não encontrada ou arquivo não autorizado")
#         except Exception as exception:
#              raise exception
#         return 0

class CriarItens(CreateView):

    model = Item
    form_class = FormularioItem
    template_name = 'item/novo.html'
    success_url = reverse_lazy('listar-itens')

class EditarItens(UpdateView):
    model = Item
    form_class = FormularioItem
    template_name = 'item/editar.html'
    success_url = reverse_lazy('listar-itens')

class DeletarItens(DeleteView):
    model = Item
    template_name = 'item/deletar.html'
    success_url = reverse_lazy('listar-itens')