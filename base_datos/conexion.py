'''
Creación BBDD a través de peewee
'''

import peewee

db = peewee.SqliteDatabase('aceites.db')

class DB(peewee.Model):

    class Meta:
        database = db