from dataclasses import fields
from django import forms
from .models import Listas, Tarefa

# Criacao dos forms, servem para criacao e edicao

# Forms das listas
class ListasForms(forms.ModelForm):
    # Atributos que devem ser passados para criacao/edicao das listas
    class Meta:
        model = Listas
        fields = ['nome']

# Forms das tarefas
class TarefaForms(forms.ModelForm):
    # O campo do atributo "data" e exibido com um widget de calendario
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )

    # Atributos que devem ser passados para criacao/edicao das tarefas
    class Meta:
        model = Tarefa
        fields = ['descricao', 'prioridade', 'data', 'feita']
