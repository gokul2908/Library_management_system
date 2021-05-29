from stocks.Books import Book

class Stock: 
    def __init__(self) -> None:
        self.sections = {}
        self.books = {}

    def insert_book(self, book: Book, sectionType = "other"):
        if self.sections(sectionType) or self.__create_new_section(sectionType):
            self.sections(sectionType).append(book)

    def no_books_in_section(self):
        for section in self.sections:
            print(f'section name: {section} available book Count: {len(self.sections[section])}')
    
    def __create_new_section(self, section_type):
        self.sections[section_type] = []
        return True

    def get_book(self, title):
        if self.books[title.lower()]:
            return True
        return False
    


        
