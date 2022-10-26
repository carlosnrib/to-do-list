from dataclasses import fields
from django import forms
from .models import Listas, Tarefa

class ListasForms(forms.ModelForm):
    class Meta:
        model = Listas
        fields = ['nome']

class TarefaForms(forms.ModelForm):
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Tarefa
        fields = ['descricao', 'prioridade', 'data', 'feita']
