from django.db import models

class Pais(models.Model):
 # catalogo/models.py



# Modelo para armazenar os países sincronizados da API externa.

    # O nome comum do país, ex: "Brasil".
    name = models.CharField(max_length=100)
    
    # O código de 2 letras (alpha-2 code), ex: "BR".
    # É 'unique=True' para garantir que não haja países duplicados.
    cca2 = models.CharField(max_length=2, unique=True, help_text="Código de 2 letras do país")
    
    # A região e sub-região, ex: "Americas", "South America".
    # 'blank=True, null=True' significa que este campo é opcional.
    region = models.CharField(max_length=100, blank=True, null=True)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    
    # A capital do país.
    capital = models.CharField(max_length=100, blank=True, null=True)
    
    # A população, que deve ser um número inteiro e positivo.
    population = models.PositiveIntegerField()
    
    # A URL para a imagem da bandeira.
    flag_url = models.URLField(max_length=255)

    # Esta função define como o objeto será exibido (ex: no painel de admin).
    def __str__(self):
        return self.name

    # 'Meta' options permitem configurar o modelo.
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['name'] # Ordena os países por nome em consultas.

# esse é o modelo para os roteiros de viagem.
class Itinerary(models.Model):
    # O título do roteiro, ex: "Praias do Nordeste".
    title = models.CharField(max_length=200, help_text="Título do Roteiro")
    
    # A CHAVE DA RELAÇÃO! Conecta este roteiro a um país.
    # Se um 'Pais' for deletado, todos os seus roteiros também serão (on_delete=models.CASCADE).
    country = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="itineraries")
    
    # As datas de início e partida da viagem.
    start_date = models.DateField(help_text="Data de início da viagem")
    departure_date = models.DateField(help_text="Data de partida da viagem")
    
    # A descrição completa do roteiro.
    description = models.TextField(help_text="Descrição detalhada do roteiro")
    
    # O preço, que é um número decimal e opcional.
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Preço do roteiro (opcional)")
    
    # Campo para upload de uma imagem de destaque.
    image = models.ImageField(upload_to='itinerary_images/', blank=True, null=True, help_text="Imagem de destaque do roteiro")

    def __str__(self):
        # Retorna um texto amigável,

        return f'{self.title} - {self.country.name}'
