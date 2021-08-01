'''
Modelo de recetas
'''

from base_datos.conexion import db

import peewee
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')


class Receta(peewee.Model):
    codigo = peewee.CharField(null=False, max_length=11, unique=True)
    contenido = peewee.CharField(max_length=150)
    fecha_creacion = peewee.DateField(default=datetime.datetime.now().strftime('%A %d de %B de %Y a las %H:%M'))
    estado = peewee.BooleanField(default=True)

    class Meta:
        db_table = 'recetas'  # nombre de la tabla de recetas
        database = db  # conexion con la BBDD
