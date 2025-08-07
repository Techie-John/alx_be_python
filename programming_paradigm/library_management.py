class Book:
    """Represents a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Checks out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Returns the book, making it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
        
    def is_available(self):
        """Returns the availability status of the book."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Manages a collection of books."""
    
    def __init__(self):
        """Initializes a Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by its title.
        Prints a message indicating success or failure.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'.")
                return
        print(f"Could not check out '{title}'. It may not be available.")

    def return_book(self, title):
        """
        Returns a book by its title.
        Prints a message indicating success or failure.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'.")
                return
        print(f"Could not return '{title}'. It may not belong to this library or is not checked out.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)