class Book:
    def __init__(self, title):
        self.title = title

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)

# Client Code
if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book(Book("Book 1"))
    collection.add_book(Book("Book 2"))

    for book in collection:
        print(book.title)


# Book 1
# Book 2