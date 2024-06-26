from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from itens.models import Item
from itens.forms import FormularioItem
from django.urls import reverse_lazy
from itens.serializers import ItemSerializer
from rest_framework import viewsets

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
    
class DetalhesItens(DetailView):

    model = Item
    template_name = 'item/detalhes.html'
    context_object_name = 'item'

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

class ItensAPI(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer