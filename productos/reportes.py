'''
Reportes de productos
'''

from productos.models import Producto


def imprimir(productos):
    for producto in productos:
        print(f"Nombre: {producto.nombre} - Descripción: {producto.descripcion} - Stock: {producto.stock} "
              f"- Código de receta: {producto.codigo_receta_id} - Código de producto: {producto.codigo} "
              f"- Precio: {producto.precio}")
    if len(productos) == 0:
        print('No se han encontrado productos con esas características.')


def buscador_productos():
    salir = True
    while salir:
        print('')
        print('-'*100)
        print('Bienvenido al buscador de productos. ¿Cómo desea realizar la búsqueda?'.center(100, ' '))
        print('-'*100)
        print('''
        1) Por nombre ó código de producto
        2) Por código de receta
        3) Salir del buscador''')

        try:
            opcion = int(input('\nEscoja opción\n>>'))
            if opcion == 1:
                valor = input('Introduce nombre/código de producto: ').upper()
                productos = Producto.select().where((Producto.nombre == valor) | (Producto.codigo == valor))
                imprimir(productos)
            elif opcion == 2:
                valor = input('Introduce código de receta: ').upper()
                productos = Producto.select().where(Producto.codigo_receta == valor)
                imprimir(productos)
            elif opcion == 3:
                salir = False
            else:
                print('Error de selección, introduzca una opción válida.')

        except ValueError:
            print('Error, debe introducir un valor numérico. Intente de nuevo.')


def reporte_productos_csv():
    productos = Producto.select().where((Producto.stock <2) & (Producto.estado == True))

    with open ('reporte_productos_sin_stock.csv','w') as fichero:
        fichero.write('Nombre, Descripción, Stock, Código de Receta, Código de producto, Precio con IVA\n')
        for producto in productos:
            fichero.write(f"{producto.nombre}, {producto.descripcion}, {producto.stock},"
                          f"{producto.codigo_receta_id}, {producto.codigo}, {round(float(producto.precio) * 1.21,2)}\n")


def reporte_productos_total_csv():
    productos = Producto.select().where(Producto.estado == True)

    with open ('reporte_productos_total.csv','w') as fichero:
        fichero.write('Nombre, Descripción, Stock, Código de Receta, Código de producto, Precio con IVA\n')
        for producto in productos:
            fichero.write(f"{producto.nombre}, {producto.descripcion}, {producto.stock},"
                          f"{producto.codigo_receta_id}, {producto.codigo}, {round(float(producto.precio) * 1.21,2)}\n")