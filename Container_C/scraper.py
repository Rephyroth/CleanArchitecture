<<<<<<< HEAD
import json 
from models import Book

with open('MOCK_DATA.json') as json_file:
    data = json.load(json_file)

for row in data:
    book = Book(id_book = row.get("id_book"),
                title = row.get("title"),
                isbn = row.get("isbn"),
                author = row.get("author"),
                publisher = row.get("publisher"),
                genre = row.get("genre"),
                num_pages = row.get("num_pages"),
                year = row.get("year")
                )

    print(f"##### Insertando registro...\n\t-> Registro: {book}\n\t-> Status: {book.save()}")

        
    
=======

import json 
from models import Book


with open('MOCK_DATA.json') as json_file:
    data = json.load(json_file)


for row in data:
    book = Book(id_book = row.get("id_book"),
                title = row.get("title"),
                isbn = row.get("isbn"),
                author = row.get("author"),
                publisher = row.get("publisher"),
                genre = row.get("genre"),
                num_pages = row.get("num_pages"),
                year = row.get("year"))
        
>>>>>>> ed9c3e59d320a6e84707768f8cb315a73a133f18
