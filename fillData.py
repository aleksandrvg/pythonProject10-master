from classLibrary.Book import Book


def CreateBooks():
    bookDict = [{"title": "Том Сойр", "author": "Марк Твен"},
                {"title": "Три Мушкетера", "author": "Александр Дюма"},
                {"title": "Сказки", "author": "Александр Пушкин"},
                {"title": "Война и мир", "author": "Лев Толстой"}]
    for row in bookDict:
        Book(title=row["title"], author=row["author"]).save()


if __name__ == "__main__":
    CreateBooks()
