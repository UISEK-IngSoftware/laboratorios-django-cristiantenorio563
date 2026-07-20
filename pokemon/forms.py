from django import forms
from .models import Pokemon, Entrenador

class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon

        fields = [
            'nombre',
            'tipo',
            'peso',
            'altura',
            'imagen',
            'video',
            'entrenador'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'tipo': forms.Select(attrs={
                'class': 'form-control'
            }),

            'peso': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'altura': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'imagen': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'video': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'entrenador': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class EntrenadorForm(forms.ModelForm):

    class Meta:
        model = Entrenador

        fields = [
            'nombre',
            'apellido',
            'ciudad',
            'imagen',
            'video'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'ciudad': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'imagen': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'video': forms.URLInput(attrs={
                'class': 'form-control'
            }),
        }
        