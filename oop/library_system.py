class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        """Initializes the book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Represents an electronic book, inheriting from Book."""

    def __init__(self, title, author, file_size):
        """Initializes an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a physical book, inheriting from Book."""

    def __init__(self, title, author, page_count):
        """Initializes a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Returns a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initializes a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book instance to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)