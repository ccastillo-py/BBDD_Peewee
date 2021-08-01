'''
Menú de selección de opción
'''

from recetas.funciones import crear_receta
from productos.funciones import crear_producto
from productos.reportes import buscador_productos, reporte_productos_csv, reporte_productos_total_csv
from recetas.reportes import buscador_recetas
from productos.modificacion import editor_productos

def menu():
    print('')
    print('#' * 100)
    print('ACEITES 2021'.center(100, ' '))
    print('- MENÚ DE SELECCIÓN -'.center(100, ' '))
    print('#' * 100)

    while not False:
        print('''
        1) Registrar receta
        2) Registrar producto
        3) Buscar producto
        4) Buscar receta
        5) Modificar producto
        6) Generar reporte de productos sin stock
        7) Generar reporte total de productos
        8) Salir del programa''')
        print('')

        try:
            opcion = int(input('Seleccione una opción: '))
            if opcion == 1:
                print('Opción elegida => Registro de receta')
                crear_receta()
            elif opcion == 2:
                print('Opción elegida => Registro de producto')
                crear_producto()
            elif opcion == 3:
                print('Opción elegida => Búsqueda de producto')
                buscador_productos()
            elif opcion == 4:
                print('Opción elegida => Búsqueda de receta')
                buscador_recetas()
            elif opcion == 5:
                print('Opción elegida => Modificación de producto')
                editor_productos()
            elif opcion == 6:
                print('Opción elegida => Generación de reporte de productos sin stock')
                reporte_productos_csv()
                print('')
                print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
                print('|*|'+'Reporte generado'.center(27,' ')+'|*|')
                print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
            elif opcion == 7:
                print('Opción elegida => Generación de reporte total de productos')
                reporte_productos_total_csv()
                print('')
                print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
                print('|*|'+'Reporte generado'.center(27,' ')+'|*|')
                print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
            elif opcion == 8:
                print('Opción elegida => Salir del programa')
                print('Saliendo del sistema...')
                break
            else:
                print('Error de selección, introduzca una opción válida.')
        except ValueError:
            print('Error, debe introducir un valor numérico. Intente de nuevo.')