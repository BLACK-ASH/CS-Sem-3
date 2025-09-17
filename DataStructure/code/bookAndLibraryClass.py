# Book Class
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn.strip()  # Removes extra whitespaces from ISBN
        self.title = title.strip()  # Removes extra whitespaces from title
        self.author = author.strip()  # Removes extra whitespaces from author
        self.available = True  # Book is available by default
        self.borrowed_by = None  # No borrower initially

    def borrow(self, name):
        # Borrow the book if it is available
        if self.available:
            self.available = False  # Mark the book as borrowed
            self.borrowed_by = name.title()  # Save borrower's name in title-case
            return True  # Return True if borrowed successfully
        return False  # Return False if already borrowed

    def return_book(self):
        # Return the book if it is currently borrowed
        if not self.available:
            self.available = True  # Mark the book as available
            self.borrowed_by = None  # Clear borrower's name
            return True  # Return True if returned successfully
        return False  # Return False if not borrowed

    def get_info(self):
        # Return formatted string with the book details
        return f"{self.title.upper()} by {self.author.upper()} - " + \
               ("Available" if self.available else f"Borrowed by {self.borrowed_by}")


# Library Class
class Library:
    def __init__(self):
        # Initialize the library with an empty dictionary of books
        self.books = {}  # Key = ISBN, Value = Book Object

    def add_book(self, book):
        # Add a book to the library if ISBN not already present
        if book.isbn not in self.books:
            self.books[book.isbn] = book  # Add book to the library dictionary
            return True  # Return True if added successfully
        return False  # Return False if ISBN already present

    def remove_book(self, isbn):
        # Remove a book by ISBN using dictionary pop()
        removed = self.books.pop(isbn, None)
        return removed is not None  # Return True if removed successfully, False otherwise

    def borrow_book(self, isbn, name):
        # Borrow a book using its ISBN and borrower's name
        book = self.books.get(isbn)  # Get the book if exists
        return book.borrow(name) if book else False  # Borrow the book if exists, False otherwise

    def return_book(self, isbn):
        # Return a book using its ISBN
        book = self.books.get(isbn)
        return book.return_book() if book else False

    def show_books(self):
        # Display all books in the library with their status
        print("Library Books List:")
        for key, book in self.books.items():  # Loop through dictionary items
            print(f"[{key}] {book.get_info()}")  # Show book details

    def search_books(self, keyword):
        # Search books by keyword in title or author (case-insensitive)
        keyword = keyword.lower()
        found = []  # List to store matching books
        for book in self.books.values():
            # Check if keyword is in title or author
            if keyword in book.title.lower() or keyword in book.author.lower():
                found.append(book)  # Add matching book to the list
        if found:
            # Sort found books by title
            found.sort(key=lambda b: b.title)
            print("Search Results:")
            for b in found:
                print(f" - {b.get_info()}")
        else:
            print("No book found with that keyword")


# Example Usage

# Create a library instance
library = Library()

# Create book instances
b1 = Book("101", "Python Programming", "John Zelle")
b2 = Book("102", "Artificial Intelligence", "Stuart Russell")
b3 = Book("103", "Data Structures", "Mark Allen Weiss")

# Add books to the library
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

# Display all books
library.show_books()

# Borrow a book with ISBN "102" by user "Alice"
library.borrow_book("102", "Alice")
print("\nAfter Borrowing:\n")
library.show_books()  # Display updated list

# Return the borrowed book with ISBN "102"
library.return_book("102")
print("\nAfter Returning:\n")
library.show_books()  # Display updated list

# Search for books by keyword "Data"
print("\nSearch by 'Data':")
library.search_books("Data")
