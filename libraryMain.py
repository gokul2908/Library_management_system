from stocks.Books import Book
from person.User import User
from person.Person import Person


class Library:
    def __init__(self) -> None:
        self.Person = []
        self.Librarin = []
        # self.Stocks = {'science':}

    def printConsole(self):
        print('''
        Follow the instructions as shown below

        ''')


# tmp = Library()
ano = User('kesav', 343, '''This is my address
         will get added''', sex='Male')
book = Book('j.k Rowling', 1200, 'Harry Potter part 1', 1.2)
print(book)
# ano.give_book()

print(ano)
