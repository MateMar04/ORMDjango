import datetime
from decimal import Decimal

from confApp.models import *


def ejercicio(n):
    print(f"\n-----EJERCICIO {n}-----")


# EJERCICIO 1

ejercicio(1)
clientes = Clientes.objects.values_list('cod_cliente', 'apellido', 'nombre').order_by('cod_cliente')
for cliente in clientes:
    print(cliente)

# EJERCICIO 2

ejercicio(2)
clientes = Clientes.objects.all().order_by('apellido', 'nombre')
for cliente in clientes:
    print(f"CODIGO: {cliente.cod_cliente}, APELLIDO: {cliente.nombre}, NOMBRE: {cliente.nombre}")

# EJERCICIO 3

ejercicio(3)
plantas = Plantas.objects.values_list('cod_planta', 'descripcion', 'precio').order_by('cod_planta')
for planta in plantas:
    print(planta)

# EJERCICIO 4

ejercicio(4)
plantas = Plantas.objects.all().order_by('descripcion')
for planta in plantas:
    print(f"DESCRIPCION: {planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 5

ejercicio(5)
localidades = Localidades.objects.all().order_by('nombre')
for localidad in localidades:
    print(localidad.nombre)

# EJERCICIO 6

ejercicio(6)
clientes = Clientes.objects.all()

# EJERCICIO 7

ejercicio(7)
plantas = Plantas.objects.all()
for planta in plantas:
    precio_off = (planta.precio - (planta.precio * Decimal(0.10))).__round__(2)
    print(
        f"CODIGO PLANTA: {planta.cod_planta}, TIPO DE PLANTA: {planta.cod_tipo_planta} DESCRIPCION: {planta.descripcion}, PRECIO: {planta.precio}, OFERTA: {precio_off}, STOCK: {planta.stock}")

# EJERCICIO 8

ejercicio(8)
plantas = Plantas.objects.all()
for planta in plantas:
    precio_total = (Decimal(planta.precio) * planta.precio).__round__(2)
    print(f"{planta.descripcion}, PRECIO: {planta.precio}, STOCK: {planta.stock} PRECIO TOTAL: {precio_total}")

# EJERCICIO 9

ejercicio(9)
deudores = Clientes.objects.all().filter(deudor='S')
for deudor in deudores:
    print(deudor.nombre)

# EJERCICIO 10

ejercicio(10)
plantas = Plantas.objects.all().filter(stock__gt=20).order_by('stock')
for planta in plantas:
    print(f"{planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 11

ejercicio(11)
plantas = Plantas.objects.all().exclude(stock=30).order_by('cod_planta')
for planta in plantas:
    print(f"{planta.descripcion}, STOCK: {planta.stock}")

# EJERCICIO 12

ejercicio(12)
facturas = Facturas.objects.all().filter(fecha__gt=datetime.date(2009, 6, 1))
for factura in facturas:
    print(f"{factura.nro_factura} {factura.fecha}")

# EJERCICIO 13

ejercicio(13)
plantas = Plantas.objects.all().filter(stock__lt=10)
for planta in plantas:
    print(f"{planta.descripcion} STOCK: {planta.stock}")

# EJERCICIO 14

ejercicio(14)
date_start = datetime.date(2008, 6, 1)
date_end = datetime.date(2010, 3, 1)
facturas = Facturas.objects.all().filter(fecha__range=(date_start, date_end))
for factura in facturas:
    print(f"{factura.nro_factura} {factura.fecha}")

# EJERCICIO 15

ejercicio(15)
plantas = Plantas.objects.all().filter(precio__range=(20, 70))
for planta in plantas:
    print(f"{planta.descripcion} {planta.precio}")

# EJERCICIO 16

ejercicio(16)
plantas = Plantas.objects.all().filter(stock__range=(5, 10))
for planta in plantas:
    print(f"{planta.descripcion} {planta.stock}")

# EJERCICIO 17

ejercicio(17)
clientes = Clientes.objects.all().filter(apellido__startswith='F')
for cliente in clientes:
    print(cliente.apellido)

# EJERCICIO 18

ejercicio(18)
clientes = Clientes.objects.all().filter(nombre__contains='U')
for cliente in clientes:
    print(cliente.nombre)

# EJERCICIO 19

ejercicio(19)
clientes = Clientes.objects.all().exclude(apellido__regex=r'^[A-C].*$')
for cliente in clientes:
    print(cliente.apellido)

# EJERCICIO 20

ejercicio(20)
clientes = Clientes.objects.all().filter(apellido__endswith='EZ')
for cliente in clientes:
    print(cliente.apellido)

# EJERCICIO 21

ejercicio(21)
clientes = Clientes.objects.all().exclude(apellido__startswith='P').order_by('apellido')
for cliente in clientes:
    print(cliente.apellido)

# EJERCICIO 22

ejercicio(22)
clientes = Clientes.objects.all().exclude(apellido__regex=r'^(P|Z)[A-Z]*').order_by('apellido')
for cliente in clientes:
    print(cliente.apellido)

# EJERCICIO 23

ejercicio(23)
clientes = Clientes.objects.all().filter(telefono__isnull=True)
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.telefono}")

# EJERCICIO 24

ejercicio(24)
clientes = Clientes.objects.all().filter(email__isnull=False)
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} {cliente.email}")

# EJERCICIO 25

ejercicio(25)
clientes = Clientes.objects.all().filter(telefono__isnull=False)
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} {cliente.nombre}")

# EJERCICIO 26

ejercicio(26)
plantas = Plantas.objects.all().filter(descripcion__startswith='R', precio__gt=7)
for planta in plantas:
    print(f"{planta.descripcion} {planta.precio}")

# EJERCICIO 27

ejercicio(27)
plantas = Plantas.objects.all().exclude(precio__gt=30, precio__lt=80).order_by('cod_planta')
for planta in plantas:
    print(f"{planta.cod_planta} {planta.descripcion} {planta.precio}")

# EJERCICIO 28

ejercicio(28)
clientes = Clientes.objects.all().exclude(email__isnull=True, telefono__isnull=True)
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} {cliente.telefono} {cliente.email}")

# EJERCICIO 29

ejercicio(29)
clientes = Clientes.objects.all().exclude(nombre__regex=r'^(M|P)[A-Z]*').exclude(apellido__startswith='B')
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.apellido}")

# EJERCICIO 30

ejercicio(30)
plantas = Plantas.objects.all().filter(stock__range=(10, 30))
for planta in plantas:
    print(f"{planta.descripcion} {planta.stock}")

# EJERCICIO 31
ejercicio(31)
clientes = Clientes.objects.all()
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} --- {cliente.cod_calle.nombre} {cliente.altura}")

# EJERCICIO 32

ejercicio(32)
clientes = Clientes.objects.all()
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} --- {cliente.cod_barrio.nombre} {cliente.cod_barrio.nombre}")

# EJERCICIO 33

ejercicio(33)
clientes = Clientes.objects.all()
for cliente in clientes:
    print(f"{cliente.apellido} {cliente.nombre} --- {cliente.cod_barrio.nombre}")

# EJERCICIO 34

ejercicio(34)
facturas = Facturas.objects.all().filter(cod_forma_pago__descripcion='EFECTIVO').order_by('cod_cliente')
for factura in facturas:
    print(f"{factura.nro_factura} --- {factura.cod_forma_pago.descripcion}")

# EJERCICIO 35

ejercicio(35)
plantas = Plantas.objects.all().filter(cod_tipo_planta__nombre='FLORES')
for planta in plantas:
    print(f"{planta.descripcion} --- {planta.cod_tipo_planta.nombre}")

# EJERCICIO 36

ejercicio(36)
clientes = Clientes.objects.all().filter(cod_localidad__nombre='AREQUITO')
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.apellido} --- {cliente.cod_localidad.nombre}")

# EJERCICIO 37

ejercicio(37)
clientes = Clientes.objects.all().filter(cod_condicion_iva__descripcion='MONOTRIBUTISTA').order_by('cod_localidad')
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre} {cliente.cod_localidad.nombre} {cliente.cod_barrio.nombre} {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")

# EJERCICIO 38

ejercicio(38)
clientes = Clientes.objects.all().filter(cod_localidad__nombre='CORDOBA', apellido__startswith='A')
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre} {cliente.cod_localidad.nombre} {cliente.cod_barrio.nombre} {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")

# EJERCICIO 39

ejercicio(39)
clientes = Clientes.objects.all().filter(cod_localidad__nombre='CORDOBA')  # REVISAR
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre}, {cliente.cod_localidad.nombre}, {cliente.cod_barrio.nombre}, {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")

# EJERCICIO 40

ejercicio(40)
clientes = Clientes.objects.all().exclude(cod_localidad__nombre='AREQUITO')  # REVISAR
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre}, {cliente.cod_localidad.nombre}, {cliente.cod_barrio.nombre}, {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")

# EJERCICIO 41

ejercicio(41)
clientes = Clientes.objects.all().filter(cod_localidad__nombre='CORDOBA').exclude(
    apellido__regex=r'^[D-P][A-Z]*').order_by('cod_barrio')
for cliente in clientes:
    print(f"{cliente.nombre} {cliente.apellido} --- {cliente.cod_barrio.nombre}")

# EJERCICIO 42

ejercicio(42)
detalles = DetallesFacturas.objects.all()
for detalle in detalles:
    precio_total = (detalle.cantidad * detalle.cod_planta.precio)
    print(f"CANTIDAD: {detalle.cantidad} PRECIO: {detalle.cod_planta.precio} PRECIO TOTAL: {precio_total}")

# EJERCICIO 43

ejercicio(43)
clientes = Clientes.objects.all().filter(cod_provincia__nombre__startswith='SAN').filter(
    cod_condicion_iva__descripcion='MONOTRIBUTISTA')
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre}, {cliente.cod_localidad.nombre}, {cliente.cod_barrio.nombre}, {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")

# EJERCICIO 44

ejercicio(44)
clientees = Clientes.objects.all().filter(cod_barrio__nombre='ALBERDI')  # REVISAR
for cliente in clientes:
    print(
        f"{cliente.cuit} --- {cliente.nombre} {cliente.apellido} --- {cliente.cod_provincia.nombre}, {cliente.cod_localidad.nombre}, {cliente.cod_barrio.nombre}, {cliente.cod_calle.nombre} {cliente.altura} --- {cliente.telefono} {cliente.email} --- {cliente.deudor} {cliente.cod_condicion_iva.descripcion}")
