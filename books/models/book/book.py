import models.book.openLibraryApi as openLibraryApi


class Book:
    id = " ",
    name = " ",
    author = " ",
    gender = " "

    def __init__(
            self,
            id,
            name,
            author,
            gender
    ):
        self.id = id,
        self.name = name,
        self.author = author,
        self.gender = gender


    @classmethod
    def get_by_name(self, name):
        list_books = openLibraryApi.get_books_by_name(name)
        return list(list_books.to_dict(orient='records'))
    
    @classmethod
    def get_book_by_key(self, book_key):
        list_books = openLibraryApi.get_book_by_key(book_key)
        return list_books


        