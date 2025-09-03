# catalogo/admin.py

from django.contrib import admin
from .models import Pais, Itinerary

# Registra o modelo Pais para que ele apareça no site de admin.
admin.site.register(Pais)

# Registra o modelo Itinerary também.
admin.site.register(Itinerary)