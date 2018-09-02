class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)

# class SciFiBookCase(Bookcase):
#     def __init__(self, books=None):
#         super().__init__(books)
#
# class RomanceBookCase(Bookcase):
#     def __init__(self, books=None):
#         super().__init__(books)
#
#
# generic_bookcase = Bookcase.create_bookcase()
#
# print generic_bookcase
# # Bookcase at x8124435234
#
# scifi = SciFiBookcase.create_bookcase()
#
# rom = RomanceBookCase.create_bookcase()
