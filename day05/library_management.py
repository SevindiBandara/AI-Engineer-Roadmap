class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'Borrowed: "{self.title}"')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        self.available = True
        print(f'Returned: "{self.title}"')

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Library Books")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book.title}")


# Create books
book1 = Book("Python Programming", "John Smith")
book2 = Book("Machine Learning Basics", "Andrew Ng")
book3 = Book("Deep Learning", "Ian Goodfellow")

# Create library
library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

print()

book1.borrow()

print()

book1.display()
book2.display()
book3.display()

print()

book1.return_book()

print()

book1.display()