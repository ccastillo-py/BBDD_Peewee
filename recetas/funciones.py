'''
Funciones de Recetas
'''

from recetas.models import Receta


def validar_codigo_receta(valor):
    try:
        codigo = Receta.get(Receta.codigo == valor)
        return codigo
    except:
        return False


def validar_estado(valor):
    while valor not in ['Y', 'N']:
        valor = input('Error; vuelve a escoger de entre las opciones [Y/N]: ').upper()
    if valor == 'Y':
        return True
    if valor == 'N':
        return False


def crear_receta():
    print('\n>> La codificación de las recetas sigue la siguiente nomenclatura: ***-***-***, donde los asteriscos')
    print('>> pueden tomar valores alfanuméricos. Las letras deberán ser mayúsculas. En caso de insertar minúsculas,')
    print('>> el sistema las convertirá directamente a caracteres válidos. No se permiten códigos nulos.')
    codigo = input('\nCódigo de la receta: ').upper()
    while (len(codigo) != 11) or (codigo[3] != '-') or (codigo[7] != '-'):
        print('Error, debe introducir un código atendiendo a la nomenclatura especificada.')
        codigo = input('Introduce de nuevo el código de la receta: ').upper()
        while validar_codigo_receta(codigo):
            print('El código de la receta ya existe.')
            codigo = input('Introduce de nuevo el código de la receta: ').upper()
    while validar_codigo_receta(codigo):
        print('El código de la receta ya existe.')
        codigo = input('Introduce de nuevo el código de la receta: ').upper()
        while (len(codigo) != 11) or (codigo[3] != '-') or (codigo[7] != '-'):
            print('Error, debe introducir un código atendiendo a la nomenclatura especificada.')
    contenido = input('Contenido de la receta: ')
    while not contenido:
        print('Este campo es obligatorio.')
        contenido = input('Contenido de la receta: ')
    estado = input('Estado [Y/N]: ').upper()
    estado = validar_estado(estado)

    receta = Receta.create(codigo=codigo, contenido=contenido, estado=estado)
    receta.save()

    print(f"\n|*| La receta {receta.codigo} ha sido creada el {receta.fecha_creacion} horas |*|")
