from django.db import models

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.OneToOneField('Vehiculo', on_delete=models.SET_NULL, null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rut})'


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.patente})'


class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    vehiculo_id = models.OneToOneField('Vehiculo', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'Registro {self.id} - {self.vehiculo_id}'
