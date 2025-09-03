from django.shortcuts import render, get_object_or_404
from .models import Pais, Itinerary
def country_list(request):

    query = request.GET.get('q', '')
    countries = Pais.objects.all()
    if query:
        countries = countries.filter(name__icontains=query)
        countries = countries.order_by('name')
    context = {
        'countries': countries,
        'search_query': query, 
          }
    
    return render(request, 'catalogo/country_list.html', context)


# view de detalhe dos paises
def country_detail(request, cca2):
    # busca um único país pelo seu código cca2.
    country = get_object_or_404(Pais, cca2=cca2)
    
    # busca todos os roteiros associados a este país.
    itineraries = country.itineraries.all()
    
    # envia o país e seus roteiros para o template.
    context = {
        'country': country,
        'itineraries': itineraries,
    }
    
    return render(request, 'catalogo/country_detail.html', context)


# view para a lista de roteiros
def itinerary_list(request):
    itineraries = Itinerary.objects.all().order_by('start_date')
    context = {
        'itineraries': itineraries
    }
    return render(request, 'catalogo/itinerary_list.html', context)


# detalhes do roteiro
def itinerary_detail(request, itinerary_id):
    #buscar o roteiro do ID
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    context = {
        'itinerary': itinerary
    }
    return render(request, 'catalogo/itinerary_detail.html', context)