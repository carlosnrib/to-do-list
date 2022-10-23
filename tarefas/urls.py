from django.urls import path
from .views import TarefasView, TarefasCreateView, TarefasUpdateView, TarefasDeleteView

urlpatterns = [
    path('', TarefasView.as_view(), name='tarefas.index'),
    path('novo/', TarefasCreateView.as_view(), name='tarefas.novo'),
    path('editar/<int:pk>', TarefasUpdateView.as_view(), name='tarefas.editar'),
    path('remover/<int:pk>', TarefasDeleteView.as_view(), name='tarefas.remover')
]