from classLibrary.BaseModel import BaseModel
from peewee import *


class User(BaseModel):
    id = PrimaryKeyField(column_name="id")
    name = CharField(column_name="name", max_length=120)
    phone = CharField(column_name="phone", max_length=15)

    class Meta:
        table_name = "user"
