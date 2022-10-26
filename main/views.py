from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Criacao da view da tela inicial
class HomeView(TemplateView):
    template_name = 'main/index.html'