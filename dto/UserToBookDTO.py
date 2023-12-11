from classLibrary.UserToBook import UserToBook
from classLibrary.User import User
from classLibrary.Book import Book
from peewee import *
import datetime


def IssuedBook(user: User, book: Book) -> UserToBook:
    dateOfGive = datetime.datetime.now().strftime("%Y-%m-%d")
    newIssued = UserToBook(date=dateOfGive, user=user, book=book)
    newIssued.save()
    return newIssued

def GetIssuedBookByUserPhone(phone: str) -> list:
    rezIssuedBook = []
    IssuedBooks = UserToBook().select().where(UserToBook.user.phone == phone).dicts
    for issuedBook in IssuedBooks:
        rezIssuedBook.append(UserToBook(id=issuedBook["id"], date=issuedBook["date"], book=issuedBook["book"]))
    return rezIssuedBook
