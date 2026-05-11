from django.urls import path
from . import views

urlpatterns = [

    path('', views.lista_pokemon, name='lista_pokemon'),

    path(
        '<int:id>/',
        views.detalle_pokemon,
        name='detalle_pokemon'
    ),

    path(
    'entrenador/<int:id>/',
    views.detalle_entrenador,
    name='detalle_entrenador'
    ),

]
