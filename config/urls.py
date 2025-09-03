from django.contrib import admin
from django.urls import path, include # Adicionei include pra chamar no path abaixo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')), 
]
