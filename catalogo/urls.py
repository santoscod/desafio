from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
    path('countries/<str:cca2>/', views.country_detail, name='country_detail'),
    # urls de roteiros
    path('itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itineraries/<int:itinerary_id>/', views.itinerary_detail, name='itinerary_detail'),
]