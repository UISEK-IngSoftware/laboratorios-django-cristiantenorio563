from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pokemon),
    path('pokemon/<int:id>/', views.detalle_pokemon),
]