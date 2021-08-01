'''
Modelo de productos
'''

import peewee

from base_datos.conexion import db
from recetas.models import Receta


class Producto(peewee.Model):
    nombre = peewee.CharField(max_length=50, unique=True)
    descripcion = peewee.CharField(max_length=150, null=True)
    stock = peewee.IntegerField(default=0)
    codigo_receta = peewee.ForeignKeyField(Receta)
    codigo = peewee.CharField(max_length=11, unique=True)
    precio = peewee.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = peewee.BooleanField(default=True)

    class Meta:
        db_table = 'productos'  # nombre de la tabla de productos
        database = db  # conexion con la BBDD
