class Book():
    def __init__(self, authorName, cost, title, name) -> None:
        self.authorName = authorName
        self.name = name
        self.cost = cost
        self.title = title
        self.borrowedDate = ''