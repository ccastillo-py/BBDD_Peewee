'''
Creación y validación de las tablas
'''

from recetas.models import Receta
from productos.models import Producto

def inicializar_tablas():
    if not Receta.table_exists():
        Receta.create_table()
    if not Producto.table_exists():
        Producto.create_table()