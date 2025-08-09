class Book:
    """A class to represent a book with magic methods."""

    def __init__(self, title, author, year):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that can be used to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"