from django.shortcuts import render
from .models import Pokemon

def lista_pokemon(request):
    pokemones = Pokemon.objects.all()
    return render(request, 'pokemon/lista.html', {'pokemones': pokemones})

def detalle_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    return render(request, 'pokemon/detalle.html', {'pokemon': pokemon})