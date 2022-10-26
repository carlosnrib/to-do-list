from audioop import reverse
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Listas, Tarefa
from .forms import ListasForms, TarefaForms

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

def tarefas(request, pk_lista):
    tarefas = Tarefa.objects.filter(lista=pk_lista)
    return render(request, 'tarefa/tarefa_list.html', {'tarefas':tarefas, 'pk_lista':pk_lista})

def tarefa_novo(request, pk_lista):
    form = TarefaForms()
    if request.method == "POST":
        form = TarefaForms(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.lista_id = pk_lista
            tarefa.save()
            return redirect(reverse('listas.tarefas', args=[pk_lista]))
    return render(request, 'tarefa/tarefa_form.html', {'form': form})

def tarefa_editar(request, pk_lista, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForms(instance=tarefa)
    if request.method == "POST":
        form = TarefaForms(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect(reverse('listas.tarefas', args=[pk_lista]))
    return render(request, 'tarefa/tarefa_form.html', {'form': form})

def tarefa_remover(request, pk_lista, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect(reverse('listas.tarefas', args=[pk_lista]))

def tarefa_executar(request, pk_lista, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if tarefa.feita == True:
        tarefa.feita = False
        tarefa.save()
    else:
        tarefa.feita = True
        tarefa.save()
    return redirect(reverse('listas.tarefas', args=[pk_lista]))

