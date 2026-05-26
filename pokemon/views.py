from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Pokemon, Entrenador
from .forms import PokemonForm, EntrenadorForm


def detalle_entrenador(request, id):

    entrenador = Entrenador.objects.get(id=id)

    return render(
        request,
        'pokemon/detalle_entrenador.html',
        {'entrenador': entrenador}
    )


def lista_pokemon(request):

    pokemones = Pokemon.objects.all()
    entrenadores = Entrenador.objects.all()

    return render(
        request,
        'pokemon/lista.html',
        {
            'pokemones': pokemones,
            'entrenadores': entrenadores
        }
    )


def detalle_pokemon(request, id):

    pokemon = get_object_or_404(
        Pokemon,
        id=id
    )

    return render(
        request,
        'pokemon/detalle.html',
        {
            'pokemon': pokemon
        }
    )


@login_required
def agregar_pokemon(request):

    if request.method == 'POST':

        form = PokemonForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = PokemonForm()

    return render(
        request,
        'pokemon/form_pokemon.html',
        {
            'form': form,
            'titulo': 'Agregar Pokémon'
        }
    )


@login_required
def editar_pokemon(request, id):

    pokemon = get_object_or_404(
        Pokemon,
        id=id
    )

    if request.method == 'POST':

        form = PokemonForm(
            request.POST,
            instance=pokemon
        )

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = PokemonForm(
            instance=pokemon
        )

    return render(
        request,
        'pokemon/form_pokemon.html',
        {
            'form': form,
            'titulo': 'Editar Pokémon'
        }
    )


@login_required
def eliminar_pokemon(request, id):

    pokemon = get_object_or_404(
        Pokemon,
        id=id
    )

    pokemon.delete()

    return redirect('/')


@login_required
def agregar_entrenador(request):

    if request.method == 'POST':

        form = EntrenadorForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = EntrenadorForm()

    return render(
        request,
        'pokemon/form_entrenador.html',
        {
            'form': form,
            'titulo': 'Agregar Entrenador'
        }
    )


@login_required
def editar_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenador,
        id=id
    )

    if request.method == 'POST':

        form = EntrenadorForm(
            request.POST,
            instance=entrenador
        )

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = EntrenadorForm(
            instance=entrenador
        )

    return render(
        request,
        'pokemon/form_entrenador.html',
        {
            'form': form,
            'titulo': 'Editar Entrenador'
        }
    )


@login_required
def eliminar_entrenador(request, id):

    entrenador = get_object_or_404(
        Entrenador,
        id=id
    )

    entrenador.delete()

    return redirect('/')


class CustomLoginView(LoginView):

    template_name = "pokemon/login_form.html"
    