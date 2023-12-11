from classLibrary.BaseModel import BaseModel
from peewee import *


class Book(BaseModel):
    id = PrimaryKeyField(column_name="id")
    title = CharField(column_name="title", max_length=120)
    author = CharField(column_name="author", max_length=120)

    class Meta:
        table_name = "book"

