from django.contrib import admin
from .models import Listas, Tarefa

# Criacao do Django Admin

# Criacao de um modelo de Admin para customizar os atributos exibidos na pagina do Django Admin
class tarefaAdmin(admin.ModelAdmin):
    # Atributos exibidos
    list_display = [
        'descricao',
        'feita',
        'prioridade',
        'data',
        'lista'
    ]

    # Filtros
    list_filter = [
        'feita',
        'prioridade',
        'data'
    ]

    # Campo de busca
    search_fields = [
        'descricao'
    ]

# Modelos exibidos na pagina do Django Admin
admin.site.register(Listas)
admin.site.register(Tarefa, tarefaAdmin)