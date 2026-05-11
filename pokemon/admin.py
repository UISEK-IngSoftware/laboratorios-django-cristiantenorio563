from django.contrib import admin
from .models import Pokemon, Entrenador


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'tipo',
        'peso',
        'altura',
        'entrenador'
    )

    search_fields = ('nombre',)


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'apellido',
        'ciudad'
    )

    search_fields = (
        'nombre',
        'apellido'
    )
    