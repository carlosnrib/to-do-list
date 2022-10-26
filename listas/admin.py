from django.contrib import admin
from .models import Listas, Tarefa

# Register your models here.

class tarefaAdmin(admin.ModelAdmin):
    list_display = [
        'descricao',
        'feita',
        'prioridade',
        'data',
        'lista'
    ]

    list_filter = [
        'feita',
        'prioridade',
        'data'
    ]

    search_fields = [
        'descricao'
    ]

admin.site.register(Listas)
admin.site.register(Tarefa, tarefaAdmin)