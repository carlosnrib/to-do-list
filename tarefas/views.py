from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarefas
from .forms import TarefasForms

class TarefasView(ListView):
    model = Tarefas
    queryset = Tarefas.objects.all().order_by('descricao')

    # Filtros
    

class TarefasCreateView(CreateView):
    model = Tarefas
    form_class = TarefasForms
    success_url = '/tarefas/'

class TarefasUpdateView(UpdateView):
    model = Tarefas
    form_class = TarefasForms
    success_url = '/tarefas/'

class TarefasDeleteView(DeleteView):
    model = Tarefas
    success_url = '/tarefas/'