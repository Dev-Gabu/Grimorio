from django import forms
from fichas.models import Ficha

class FormularioFicha(forms.ModelForm):

    class Meta:
        model = Ficha
        exclude = []