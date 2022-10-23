from django import forms
from .models import Tarefas

class TarefasForms(forms.ModelForm):
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    
    class Meta:
        model = Tarefas
        fields = ['descricao', 'prioridade', 'data', 'feita']