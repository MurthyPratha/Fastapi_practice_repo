from fastapi import FastAPI
from models import LocalBook


lbook = [LocalBook(id=1,name='Happy Pottrt and The stone',author="J.K.Rowling",year=2001),
         LocalBook(id=2,name='Happy Pottrt and The Secreat of chanbers',author="J.K.Rowling",year=2002),
         LocalBook(id=3,name='Happy Pottrt and The Other of Phenix',author="J.K.Rowling",year=2004),
         LocalBook(id=4,name='Happy Pottrt and The Goblet of fire',author="J.K.Rowling",year = 2005)]





app = FastAPI()

@app.get("/")
def greet():
    return 'Hello bhai'


@app.get("/books")
def get_all_books():
    return lbook

@app.get("/book/{id}")
def get_book_by_id(id:int):
    for book in lbook:
        if book.id == id:
            return lbook[id-1]
    return 'The Book is not found'