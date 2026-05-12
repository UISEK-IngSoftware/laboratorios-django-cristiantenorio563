from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.lista_pokemon,
        name='lista_pokemon'
    ),

    path(
        'pokemon/<int:id>/',
        views.detalle_pokemon,
        name='detalle_pokemon'
    ),

    path(
        'agregar-pokemon/',
        views.agregar_pokemon,
        name='crear_pokemon'
    ),

    path(
        'editar-pokemon/<int:id>/',
        views.editar_pokemon,
        name='editar_pokemon'
    ),

    path(
        'eliminar-pokemon/<int:id>/',
        views.eliminar_pokemon,
        name='eliminar_pokemon'
    ),

    path(
        'agregar-entrenador/',
        views.agregar_entrenador,
        name='crear_entrenador'
    ),

    path(
        'editar-entrenador/<int:id>/',
        views.editar_entrenador,
        name='editar_entrenador'
    ),

    path(
        'eliminar-entrenador/<int:id>/',
        views.eliminar_entrenador,
        name='eliminar_entrenador'
    ),

    path(
        'entrenador/<int:id>/',
        views.detalle_entrenador,
        name='detalle_entrenador'
    ),
]
