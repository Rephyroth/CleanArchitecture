import json 
from models import Book

def get_books_from_file():
    with open('MOCK_DATA.json') as json_file:
        data = json.load(json_file)
        return data

def insert_bd(data):
    for row in data:
        book = Book(id_book = row.get("id_book"),
                    title = row.get("title"),
                    isbn = row.get("isbn"),
                    author = row.get("author"),
                    publisher = row.get("publisher"),
                    genre = row.get("genre"),
                    num_pages = row.get("num_pages"),
                    year = row.get("year"))
        
    
