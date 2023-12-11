from classLibrary.Book import Book
from peewee import *


def GetAllBook() -> list:
    books = Book.select().dicts()
    rezBooks = []
    for book in books:
        rezBooks.append(Book(id=book["id"], title=book["title"], author=book["author"]))
    return rezBooks

def GetBookById(inId:int) -> Book:
    book = Book.select().where(Book.id == inId).get()
    return book
