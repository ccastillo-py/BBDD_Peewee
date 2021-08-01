'''
Modificación de productos
'''

from productos.models import Producto
from productos.funciones import validar_nombre_producto, validar_codigo_producto
from recetas.funciones import validar_estado, validar_codigo_receta


def editor_productos():
    salir = True
    while salir:
        print('')
        print('-'*100)
        print('Bienvenido al editor de productos. ¿Qué desea realizar?'.center(100, ' '))
        print('-'*100)
        print('''
        1) Modificar un producto
        2) Salir del editor''')

        try:
            opcion = int(input('\nEscoja opción\n>>'))
            if opcion == 1:
                print('>> Se reasignarán los valores anteriores en caso de no introducir valores en todos los'
                      ' campos siguiente:')
                print('>> NOMBRE - DESCRIPCION - STOCK - PRECIO')
                valor = input('\nIntroduce código de producto a modificar: ').upper()

                while not valor:
                    print('El código del producto no existe o es nulo.')
                    valor = input('Introduce de nuevo el código del producto: ').upper()
                    while not validar_codigo_producto(valor):
                        print('El código del producto no existe o es nulo.')
                        valor = input('Introduce de nuevo el código del producto: ').upper()
                while not validar_codigo_producto(valor):
                    print('El código del producto no existe.')
                    valor = input('Introduce de nuevo el código del producto: ').upper()
                    while not valor:
                        print('El código del producto no puede ser nulo.')
                        valor = input('Introduce de nuevo el código del producto: ').upper()

                producto = Producto.get(Producto.codigo == valor)

                producto.nombre = input('\nNombre del producto actualizado: ').upper()
                while validar_nombre_producto(producto.nombre):
                    print('El nombre del producto ya existe.')
                    producto.nombre = input('Nombre del producto actualizado: ').upper()
                producto.descripcion = input('Descripción actualizada: ')
                producto.stock = input('Stock actualizado: ')
                producto.codigo_receta_id = input('Código de la receta actualizado: ').upper()
                while not validar_codigo_receta(producto.codigo_receta_id):
                    print('El código de la receta no existe.')
                    producto.codigo_receta_id = input('Código de la receta actualizado: ').upper()
                producto.codigo = input('Código del producto actualizado: ').upper()

                while not producto.codigo:
                    print('El código del producto no puede ser nulo.')
                    producto.codigo = input('Introduce de nuevo el código del producto actualizado: ').upper()
                    while validar_codigo_producto(producto.codigo):
                        print('El código del producto ya existe.')
                        producto.codigo = input('Código del producto actualizado: ').upper()
                while validar_codigo_producto(producto.codigo):
                    print('El código del producto ya existe.')
                    producto.codigo = input('Código del producto actualizado: ').upper()
                    while not producto.codigo:
                        print('El código del producto no puede ser nulo.')
                        producto.codigo = input('Introduce de nuevo el código del producto: ').upper()

                producto.precio = (input('Precio actualizado: '))
                producto.estado = input('Estado actualizado [Y/N]: ').upper()
                producto.estado = validar_estado(producto.estado)

                if (not producto.nombre) and (not producto.descripcion) and (not producto.stock)\
                        and (not producto.precio):
                    producto = Producto.get(Producto.codigo == valor)

                producto.save()
                print(f"Nombre: {producto.nombre} - Descripción: {producto.descripcion} - Stock: {producto.stock} "
                      f"- Código de receta: {producto.codigo_receta_id} - Código de producto: {producto.codigo} "
                      f"- Precio: {producto.precio}")
            elif opcion == 2:
                salir = False
            else:
                print('Error de selección, introduzca una opción válida.')

        except ValueError:
            print('Error, debe introducir un valor numérico. Intente de nuevo.')