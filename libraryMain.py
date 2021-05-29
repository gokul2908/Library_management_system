from person.Person import Person


class Library:
    def __init__(self) -> None:
        self.Books = []
        self.Person = []
        self.Librarin = []

    def printConsole(self):
        print('''
        Follow the instructions as shown below

        ''')


tmp = Library()
ano = Person('kesav', 343, '''This is my address
         will get added''', sex='Male' )

print(ano)

