from .models import Chofer, Vehiculo, RegistroContabilidad
from datetime import date

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save()
    return vehiculo

def crear_chofer(rut, nombre, apellido, activo=False, vehiculo_id=None):
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo, vehiculo_id=vehiculo_id)
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo):
    registro = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo_id=vehiculo)
    registro.save()
    return registro

def deshabilitar_chofer(chofer):
    chofer.activo = False
    chofer.save()

def deshabilitar_vehiculo(vehiculo):
    vehiculo.delete()

def habilitar_chofer(chofer):
    chofer.activo = True
    chofer.save()

def habilitar_vehiculo(patente, marca, modelo, year):
    return crear_vehiculo(patente, marca, modelo, year)

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)

def asignar_chofer_a_vehiculo(chofer, vehiculo):
    chofer.vehiculo_id = vehiculo
    chofer.save()

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for v in vehiculos:
        print(f'{v.patente} - {v.marca} {v.modelo} ({v.year})')
