from django.urls import path
from .views import ListasCreateView, ListasDeleteView, ListasUpdateView, ListasView


urlpatterns = [
    path('', ListasView.as_view(), name='listas.index'),
    path('novo/', ListasCreateView.as_view(), name='listas.novo'),
    path('editar/<int:pk>', ListasUpdateView.as_view(), name='listas.editar'),
    path('remover/<int:pk>', ListasDeleteView.as_view(), name='listas.remover')
]
