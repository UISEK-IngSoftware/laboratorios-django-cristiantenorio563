from django.db import models

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()
    entrenador = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre