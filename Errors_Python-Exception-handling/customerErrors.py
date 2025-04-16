#This program shows to create your own errors which are specific and relvant to ur scenario and easier to read

class TooManyPagesError(Exception):
    pass


class Book:
    def __init__(self, name: str, pages: int):
        self.name = name
        self.pages = pages
        self.page_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.page_read} pages out of {self.pages} pages>"
        )
    def read(self, pages_done: int):
        if self.page_read + pages_done > self.pages:
            raise TooManyPagesError(
                f"You tried to read {self.page_read+pages_done} pages but total pages in books are {self.pages} pages"
            )
        self.page_read+=pages_done
        print(f"You have now read {self.page_read} out of {self.pages} pages")


try:
    book1 = Book("Harry Potter",100)
    book2 = Book("James Bond",50)
    book2.read(50)
    book1.read(50)
except TooManyPagesError as e:
    print(e)

