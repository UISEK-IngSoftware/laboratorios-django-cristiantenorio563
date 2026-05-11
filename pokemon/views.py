from django.shortcuts import render, get_object_or_404

from .models import Pokemon, Entrenador


def lista_pokemon(request):

    pokemones = Pokemon.objects.all()

    entrenadores = Entrenador.objects.all()

    contexto = {
        'pokemones': pokemones,
        'entrenadores': entrenadores
    }

    return render(
        request,
        'pokemon/lista.html',
        contexto
    )


def detalle_pokemon(request, id):

    pokemon = get_object_or_404(Pokemon, id=id)

    return render(
        request,
        'pokemon/detalle.html',
        {'pokemon': pokemon}
    )

def detalle_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenador,
        id=id
    )

    return render(
        request,
        'pokemon/detalle_entrenador.html',
        {'entrenador': entrenador}
    )