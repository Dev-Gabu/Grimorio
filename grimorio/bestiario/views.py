from grimorio.bibliotecas import LoginObrigatorio
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from bestiario.models import Criatura
from bestiario.forms import FormularioCriatura
from django.urls import reverse_lazy
from bestiario.serializers import CriaturaSerializer
from rest_framework import viewsets

class ListarCriaturas(ListView):

    model = Criatura
    context_object_name = 'criaturas'
    template_name = 'bestiario/listar.html'

    def get_queryset(self, **kwargs):
        queryset =  Criatura.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            query = queryset.filter(modelo_icontains=pesquisa)
        return queryset
    
class DetalhesCriaturas(DetailView):
    model = Criatura
    template_name = 'bestiario/detalhes.html'
    context_object_name = 'criatura'

class CriarCriaturas(CreateView):

    model = Criatura
    form_class = FormularioCriatura
    template_name = 'bestiario/novo.html'
    success_url = reverse_lazy('listar-criaturas')

class EditarCriaturas(UpdateView):
    model = Criatura
    form_class = FormularioCriatura
    template_name = 'bestiario/editar.html'
    success_url = reverse_lazy('listar-criaturas')

class DeletarCriaturas(DeleteView):
    model = Criatura
    template_name = 'bestiario/deletar.html'
    success_url = reverse_lazy('listar-criaturas')

class CriaturasAPI(viewsets.ModelViewSet):
    queryset = Criatura.objects.all()
    serializer_class = CriaturaSerializer