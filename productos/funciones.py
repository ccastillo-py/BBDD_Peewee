'''
Funciones de Productos
'''

from productos.models import Producto
from recetas.funciones import validar_codigo_receta, validar_estado


def validar_codigo_producto(valor):
    try:
        codigo = Producto.get(Producto.codigo == valor)
        return codigo
    except:
        return False


def validar_nombre_producto(valor):
    try:
        nombre = Producto.get(Producto.nombre == valor)
        return nombre
    except:
        return False


def crear_producto():
    print('\n>> No pueden repetirse nombres ni dejar el campo vacío.')
    nombre = input('\nNombre del producto: ').upper()
    while not nombre:
        print('El nombre del producto no puede estar vacío.')
        nombre = input('Introduce de nuevo el nombre del producto: ').upper()
        while validar_nombre_producto(nombre):
            print('El nombre del producto ya existe o no puede estar vacío.')
            nombre = input('Nombre del producto: ').upper()
    while validar_nombre_producto(nombre):
        print('El nombre del producto ya existe.')
        nombre = input('Nombre del producto: ').upper()
        while not nombre:
            print('El nombre del producto ya existe o no puede estar vacío.')
            nombre = input('Introduce de nuevo el nombre del producto: ').upper()
    descripcion = input('Descripción: ')
    stock = int(input('Stock: '))
    codigo_receta = input('Código de la receta: ').upper()
    while not validar_codigo_receta(codigo_receta):
        print('El código de la receta no existe.')
        codigo_receta = input('Código de la receta: ').upper()
    codigo = input('Código del producto: ').upper()
    while not codigo:
        print('El código del producto no puede ser nulo.')
        codigo = input('Introduce de nuevo el código del producto: ').upper()
        while validar_codigo_producto(codigo):
            print('El código del producto ya existe.')
            codigo = input('Código del producto: ').upper()
    while validar_codigo_producto(codigo):
        print('El código del producto ya existe.')
        codigo = input('Código del producto: ').upper()
        while not codigo:
            print('El código del producto no puede ser nulo.')
            codigo = input('Introduce de nuevo el código del producto: ').upper()

    precio = (input('Precio: '))
    estado = input('Estado [Y/N]: ').upper()
    estado = validar_estado(estado)

    producto = Producto.create(nombre=nombre, descripcion=descripcion, stock=stock,
                               codigo_receta=codigo_receta, codigo=codigo, precio=precio, estado=estado)
    producto.save()

    print(f"\n|*| El producto {producto.nombre} con código {producto.codigo} ha sido creado |*|")
