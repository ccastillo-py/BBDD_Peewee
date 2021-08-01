'''
Reportes de recetas
'''

from recetas.models import Receta

def imprimir(recetas):
    for receta in recetas:
        print(f"Código: {receta.codigo} - Contenido: {receta.contenido} "
              f"- Fecha de creación: {receta.fecha_creacion} - Estado: {receta.estado}")
    if len(recetas) == 0:
        print('No se han encontrado recetas con esas características.')

def buscador_recetas():
    salir = True
    while salir:
        print('')
        print('-'*100)
        print('Bienvenido al buscador de recetas. ¿Qué desea realizar?'.center(100, ' '))
        print('-'*100)
        print('''
        1) Búsqueda de receta por código
        2) Salir del buscador''')

        try:
            opcion = int(input('\nEscoja opción\n>>'))
            if opcion == 1:
                valor = input('Introduce código de receta: ').upper()
                recetas = Receta.select().where(Receta.codigo == valor)
                imprimir(recetas)
            elif opcion == 2:
                salir = False
            else:
                print('Error de selección, introduzca una opción válida.')

        except ValueError:
            print('Error, debe introducir un valor numérico. Intente de nuevo.')