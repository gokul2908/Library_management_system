from stocks.Books import Book
from person.Person import Person
from datetime import datetime

class User(Person):
    __Max_book_count = 3
    def __init__(self, name, age, address, sex) -> None:
        super().__init__(name, age, address, sex)
        self.books = []
        self.borrowed_books_history: dict[str, list[datetime]] = {}

    def give_book(self, book: Book):

        if len(self.books) < User.__Max_book_count and not self.is_user_got_book_within_30_days(book.name):

            self.books.append(book)

            return True

        return False

    def is_user_got_book_within_30_days(self, bookName: str):

        currentBook = self.borrowed_books_history(bookName)

        if not currentBook or (currentBook[len(currentBook) - 1] - datetime.now()).days > 30:
             return False

        return True







    