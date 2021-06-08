from peewee import CharField, Model, PrimaryKeyField
from db import db

class Book(Model):
    id_book = PrimaryKeyField()
    title = CharField()
    isbn = CharField()
    author = CharField()
    publisher = CharField()
    genre = CharField()
    num_pages = CharField()
    year = CharField()

    class Meta:
        database = db
        table_name = "book"
        
    

