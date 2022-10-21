from decimal import Decimal

from confApp.models import *

# EJERCICIO 1

clientes = Clientes.objects.values_list('cod_cliente', 'apellido', 'nombre').order_by('cod_cliente')
for cliente in clientes:
    print(cliente)

# EJERCICIO 2

clientes = Clientes.objects.all().order_by('apellido', 'nombre')
for cliente in clientes:
    print(f"CODIGO: {cliente.cod_cliente}, APELLIDO: {cliente.nombre}, NOMBRE: {cliente.nombre}")

# EJERCICIO 3

plantas = Plantas.objects.values_list('cod_planta', 'descripcion', 'precio').order_by('cod_planta')
for planta in plantas:
    print(planta)

# EJERCICIO 4

plantas = Plantas.objects.all().order_by('descripcion')
for planta in plantas:
    print(f"DESCRIPCION: {planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 5

localidades = Localidades.objects.all().order_by('nombre')
for localidad in localidades:
    print(localidad.nombre)

# EJERCICIO 6

clientes = Clientes.objects.all()

# EJERCICIO 7

plantas = Plantas.objects.all()
for planta in plantas:
    precio_off = (planta.precio - (planta.precio * Decimal(0.10))).__round__(2)
    print(
        f"CODIGO PLANTA: {planta.cod_planta}, TIPO DE PLANTA: {planta.cod_tipo_planta} DESCRIPCION: {planta.descripcion}, PRECIO: {planta.precio}, OFERTA: {precio_off}, STOCK: {planta.stock}")

# EJERCICIO 8
plantas = Plantas.objects.all()
for planta in plantas:
    precio_total = (Decimal(planta.precio) * planta.precio).__round__(2)
    print(f"{planta.descripcion}, PRECIO: {planta.precio}, STOCK: {planta.stock} PRECIO TOTAL: {precio_total}")
