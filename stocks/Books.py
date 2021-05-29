class Book:

    __options = ["authorName", "cost", "title", "borrowedDate", "version"]

    def __init__(self, authorName, cost, title, version=0) -> None:
        self.details = {'authorName': authorName,
                        'cost': cost, 'title': title, 'version': version}

    def edit(self):
        try:
            sub = int(input(
                """enter 1 for cost
                2 for author name
                3 for title
                4 for version
                5 to edit all the above:
            """
            ))
            if sub < 5:
                self.details[Book.__options[sub - 1]] = input()
            elif sub == 5:
                for option in Book.__options:
                    self.details[option] = input()

        except:
            print('Enter denoted values')
            self.edit()

    def __str__(self) -> str:
        return f'Book details: {self.details}'
