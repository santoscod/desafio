# catalogo/management/commands/sync_countries.py

from django.core.management.base import BaseCommand
import requests
from catalogo.models import Pais

class Command(BaseCommand):
    help = 'Sincroniza os países da API REST Countries para o banco de dados local.'

    # URL da API REST Countries com os campos que precisamos.
    API_URL = "https://restcountries.com/v3.1/all?fields=name,cca2,region,subregion,capital,population,flags"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando a sincronização de países...'))

        try:
            # 1. FAZ A REQUISIÇÃO PARA A API
            response = requests.get(self.API_URL)
            # Levanta um erro caso a requisição não seja bem-sucedida (ex: erro 404, 500)
            response.raise_for_status()
            
            # Pega a lista de países do JSON da resposta.
            countries_data = response.json()
            
            # 2. ITERA SOBRE OS DADOS E SALVA NO BANCO
            for country_data in countries_data:
                # O método update_or_create é perfeito para isso:
                # - Ele tenta encontrar um País com o cca2 correspondente.
                # - Se encontrar, atualiza os campos com os novos dados (defaults).
                # - Se NÃO encontrar, cria um novo registro de País.
                Pais.objects.update_or_create(
                    cca2=country_data['cca2'],
                    defaults={
                        'name': country_data['name']['common'],
                        'region': country_data.get('region', ''),
                        'subregion': country_data.get('subregion', ''),
                        'capital': country_data.get('capital', [''])[0] if country_data.get('capital') else '',
                        'population': country_data['population'],
                        'flag_url': country_data['flags']['svg']
                    }
                )
            
            self.stdout.write(self.style.SUCCESS(f'{len(countries_data)} países foram sincronizados com sucesso!'))

        except requests.RequestException as e:
            # Captura erros de conexão com a API (ex: sem internet)
            self.stdout.write(self.style.ERROR(f'Erro ao acessar a API: {e}'))