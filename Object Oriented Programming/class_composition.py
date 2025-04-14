class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"
    
book  = Book("Python Programming")
book1 = Book("Java Programming")
book2 = Book("C++ Programming")

shelf = BookShelf(book, book1, book2)
print(shelf)  # Output: Bookshelf with 3 books.

bookinfo = [str(book) for book in shelf.books]
print(bookinfo)  # Output: ['Book: Python Programming', 'Book: Java Programming', 'Book: C++ Programming']

#inheritance means a book is a bookshelf
#composition means a shelf has many books