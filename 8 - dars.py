class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books
    
    def find_books(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def update_book (self, old_title, new_book):

        for i, book in enumerate(self.books):
            if book.title == old_title:
                self.books[i] = new_book
                return True
        return False
    
    def delete_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                return True
        return False
    
class LibraryContextManager:
    def __init__(self, library):
        self.library = library

    def __enter__(self):
        return self.library
    
    def __exit__(self, exc_type, exc_val, exc_tb):
          if self.conn:
            self.conn.close()

          if self.cur:
            self.cur.close()

library = Library()

with LibraryContextManager(library) as lib:
    book1 = Book("Tib qonunlari, Ibn Sino, 905")
    book2 = Book("xamsa, Alisher Navoiy, 1483-1485")

    lib.add_book(book1)
    lib.add_book(book2)

    print(lib.get_books())

    update_book = Book("Tib Qonunlar, Ibn Sino, 909")
    lib.update_book("909, updated_book")
    print(lib.get_books())

    lib.delete_book("xamsa")
    print(lib.get_books())