import datetime
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

# EJERCICIO 9

deudores = Clientes.objects.all().filter(deudor='S')
for deudor in deudores:
    print(deudor.nombre)

# EJERCICIO 10

plantas = Plantas.objects.all().filter(stock__gt=20).order_by('stock')
for planta in plantas:
    print(f"{planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 11

plantas = Plantas.objects.all().exclude(stock=30).order_by('cod_planta')
for planta in plantas:
    print(f"{planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 12

facturas = Facturas.objects.all().filter(fecha__gt=datetime.date(2009, 6, 1))
for factura in facturas:
    print(f"{factura.nro_factura} {factura.fecha}")

# EJERCICIO 13

plantas = Plantas.objects.all().filter(stock__lt=10)
for planta in plantas:
    print(f"{planta.descripcion} STOCK: {planta.stock}")

# EJERCICIO 14

date_start = datetime.date(2008, 6, 1)
date_end = datetime.date(2010, 3, 1)
facturas = Facturas.objects.all().filter(fecha__range=(date_start, date_end))
for factura in facturas:
    print(f"{factura.nro_factura} {factura.fecha}")

# EJERCICIO 15

plantas = Plantas.objects.all().filter(precio__range=(20, 70))
for planta in plantas:
    print(f"{planta.descripcion} {planta.precio}")

# EJERCICIO 16
plantas = Plantas.objects.all().filter(stock__range=(5, 10))
for planta in plantas:
    print(f"{planta.descripcion} {planta.stock}")
