
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
        
