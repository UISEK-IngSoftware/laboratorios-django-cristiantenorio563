from django.urls import path, include
from rest_framework import routers
from .views import PokemonViewSet, EntrenadorViewSet

router = routers.DefaultRouter()
router.register(r'pokemons', PokemonViewSet)
router.register(r'entrenadores', EntrenadorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
