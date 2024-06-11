from django import forms
from itens.models import Item

class FormularioItem(forms.ModelForm):

    class Meta:
        model = Item
        exclude = []