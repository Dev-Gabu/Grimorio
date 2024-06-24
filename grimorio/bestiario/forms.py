from django import forms
from bestiario.models import Criatura

class FormularioCriatura(forms.ModelForm):

    class Meta:
        model = Criatura
        exclude = []