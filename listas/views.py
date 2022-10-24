from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Listas
from .forms import ListasForms

class ListasView(ListView):
    model = Listas
    queryset= Listas.objects.all().order_by('nome')

class ListasCreateView(CreateView):
    model = Listas
    form_class= ListasForms
    success_url= '/listas/'

class ListasUpdateView(UpdateView):
    model = Listas
    form_class= ListasForms
    success_url= '/listas/'

class ListasDeleteView(DeleteView):
    model = Listas
    success_url= '/listas/'
