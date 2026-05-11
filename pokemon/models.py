from django.db import models


class Entrenador(models.Model):

    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    ciudad = models.CharField(max_length=50)

    imagen = models.URLField()

    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pokemon(models.Model):

    TIPOS = [
        ('Agua', 'Agua'),
        ('Fuego', 'Fuego'),
        ('Planta', 'Planta'),
        ('Eléctrico', 'Eléctrico'),
        ('Tierra', 'Tierra'),
    ]

    nombre = models.CharField(max_length=50)

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    altura = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.CASCADE
    )

    imagen = models.URLField()

    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
