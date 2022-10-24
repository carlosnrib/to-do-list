from django import forms
from .models import Listas

class ListasForms(forms.ModelForm):
    class Meta:
        model = Listas
        fields = ['nome']