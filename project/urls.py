from django.contrib import admin
from django.urls import path, include

# Todas as urls do programa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('listas/', include('listas.urls')),
]
