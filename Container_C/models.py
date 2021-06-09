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
        
    

    def __str__(self):
        return f"ID: {self.id_book} - Title: {self.title} - isbn: {self.isbn} -author {self.author} - publisher: {self.publisher} - genre: {self.genre} - num_pages: {self.num_pages} - year: {self.year}"

