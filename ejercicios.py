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


