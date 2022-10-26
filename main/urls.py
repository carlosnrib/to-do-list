from django.urls import path
from .views import HomeView

# Criacao da url da tela inicial
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]