from dto import UserDTO, BookDTO, UserToBookDTO
from classLibrary.User import User


def regUser() -> User:
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    return UserDTO.RegistrationUser(phone, name)

def SeeAllBook() -> str:
    _book = ""
    books = BookDTO.GetAllBook()
    for book in books:
        _book += f"{book.id} {book.title} {book.author}\n"
    return _book

def IssueBook():
    userPhone = input("Введите номер телефона: ")
    try:
        user = UserDTO.GetUserByPhone(userPhone)
    except Exception:
        user = regUser()
    try:
        bookId = int(input("Введите номер книги: "))
        book = BookDTO.GetBookById(bookId)
        issueBook = UserToBookDTO.IssuedBook(user, book)
    except Exception:
        print("Не удалось выдать книгу")

_mainMenu = ""
while True:
    _mainMenu = "1 - зарегистрировать пользователя, 2 - посмотреть все книги, 3 - выдать книгу"
    choise = input(_mainMenu)
    if choise == "1":
        regUser()
    elif choise == "2":
        print(SeeAllBook())
    elif choise == "3":
        IssueBook()
    else:
        continue
