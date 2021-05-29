class Book():
    def __init__(self, authorName, cost, title, name, version = 0) -> None:
        self.authorName = authorName
        self.name = name
        self.cost = cost
        self.title = title
        self.borrowedDate = ''
        self.version = version
