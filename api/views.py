from rest_framework import viewsets
from .serializers import PokemonSerializer  
from pokemon.models import Pokemon
# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    