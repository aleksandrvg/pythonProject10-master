from classLibrary.User import User
from peewee import *


def RegistrationUser(phone: str, name: str) -> User:
    newUser = User(phone=phone, name=name)
    newUser.save()
    return newUser

def GetUserByPhone(phoneIn: str) -> User:
    user = User.select().where(User.phone == phoneIn).get()
    return user
