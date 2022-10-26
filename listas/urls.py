from django.urls import path
from .views import ListasCreateView, ListasDeleteView, ListasUpdateView, ListasView
from . import views

# Urls utilizadas nas paginas das listas e das tarefas
# Aqui estao as urls de exibicao, criacao, edicao e remocao de listas e tarefas
urlpatterns = [
    path('', ListasView.as_view(), name='listas.index'),
    path('novo/', ListasCreateView.as_view(), name='listas.novo'),
    path('<int:pk>/editar', ListasUpdateView.as_view(), name='listas.editar'),
    path('<int:pk>/remover', ListasDeleteView.as_view(), name='listas.remover'),
    path('<int:pk_lista>/tarefas', views.tarefas, name='listas.tarefas'),
    path('<int:pk_lista>/tarefas/novo', views.tarefa_novo, name='tarefa.novo'),
    path('<int:pk_lista>/tarefas/<int:pk>/editar', views.tarefa_editar, name='tarefa.editar'),
    path('<int:pk_lista>/tarefas/<int:pk>/remover', views.tarefa_remover, name='tarefa.remover'),
    path('<int:pk_lista>/tarefas/<int:pk>/executar', views.tarefa_executar, name='tarefa.executar'),
]
