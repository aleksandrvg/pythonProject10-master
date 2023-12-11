from classLibrary.BaseModel import BaseModel
from classLibrary.User import User
from classLibrary.Book import Book
from peewee import *


class UserToBook(BaseModel):
    id = PrimaryKeyField(column_name="id")
    user = ForeignKeyField(User, related_name="user_id_user_to_book", to_field="id")
    book = ForeignKeyField(Book, related_name="book_id_user_to_book", to_field="id")
    date = DateField(column_name="date_of_give")

    class Meta:
        table_name = "user_to_book"
