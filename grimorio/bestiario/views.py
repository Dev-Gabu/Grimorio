from grimorio.bibliotecas import LoginObrigatorio
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from bestiario.models import Criatura
from bestiario.forms import FormularioCriatura
from django.urls import reverse_lazy

class ListarCriaturas(ListView):

    model = Criatura
    context_object_name = 'critaturas'
    template_name = 'bestiario/listar.html'

    def get_queryset(self, **kwargs):
        queryset =  Criatura.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            query = queryset.filter(modelo_icontains=pesquisa)
        return queryset

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