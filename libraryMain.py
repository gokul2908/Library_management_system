from person.User import User
from person.Person import Person


class Library:
    def __init__(self) -> None:
        self.Person = []
        self.Librarin = []
        self.Stocks = {'science': }

    def printConsole(self):
        print('''
        Follow the instructions as shown below

        ''')


tmp = Library()
ano = User('kesav', 343, '''This is my address
         will get added''', sex='Male' )
# ano.give_book()

print(ano)
