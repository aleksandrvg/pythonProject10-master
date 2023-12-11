from classLibrary.UserToBook import UserToBook
from classLibrary.Book import Book
from classLibrary.User import User


if __name__ == "__main__":
    status = "OK"
    try:
        UserToBook.drop_table()
        Book.drop_table()
        User.drop_table()
    except Exception as e:
        status = f"Drop error, {e}"
    try:
        User.create_table()
        Book.create_table()
        UserToBook.create_table()
    except Exception as e:
        status = f"Create error, {e}"
    print(f"Migration {status}")
