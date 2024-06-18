from typing import List, Dict, Optional

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    """A class representing a member of the library."""

    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.checked_out_books: List[Book] = []

    def __str__(self) -> str:
        return f"Member: {self.name}, ID: {self.member_id}"


class Library:
    """A class representing the library."""

    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}

    def add_book(self, book: Book) -> None:
        """Add a book to the library."""
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists in the library.")
        self.books[book.isbn] = book
        print(f"Added {book}")

    def register_member(self, member: Member) -> None:
        """Register a new member."""
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} already exists.")
        self.members[member.member_id] = member
        print(f"Registered {member}")

    def check_out_book(self, isbn: str, member_id: str) -> None:
        """Check out a book to a member."""
        if isbn not in self.books:
            raise ValueError(f"No book with ISBN {isbn} found in the library.")
        if member_id not in self.members:
            raise ValueError(f"No member with ID {member_id} found in the library.")
        
        book = self.books[isbn]
        member = self.members[member_id]

        if book.is_checked_out:
            raise ValueError(f"The book {book.title} is already checked out.")
        
        book.is_checked_out = True
        member.checked_out_books.append(book)
        print(f"{member.name} checked out {book.title}")

    def return_book(self, isbn: str, member_id: str) -> None:
        """Return a checked-out book."""
        if isbn not in self.books:
            raise ValueError(f"No book with ISBN {isbn} found in the library.")
        if member_id not in self.members:
            raise ValueError(f"No member with ID {member_id} found in the library.")
        
        book = self.books[isbn]
        member = self.members[member_id]

        if book not in member.checked_out_books:
            raise ValueError(f"The book {book.title} is not checked out by {member.name}.")

        book.is_checked_out = False
        member.checked_out_books.remove(book)
        print(f"{member.name} returned {book.title}")

    def list_books(self) -> None:
        """List all books in the library."""
        print("Library books:")
        for book in self.books.values():
            status = "Checked out" if book.is_checked_out else "Available"
            print(f"{book} - {status}")

    def list_members(self) -> None:
        """List all members of the library."""
        print("Library members:")
        for member in self.members.values():
            print(member)
            for book in member.checked_out_books:
                print(f" - {book}")


def main() -> None:
    """Main function to demonstrate the library system."""
    library = Library()

    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "0987654321")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "1122334455")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    library.register_member(member1)
    library.register_member(member2)

    # List books and members
    library.list_books()
    library.list_members()

    # Check out and return books
    library.check_out_book("1234567890", "M001")
    library.check_out_book("0987654321", "M002")

    library.list_books()
    library.list_members()

    library.return_book("1234567890", "M001")

    library.list_books()
    library.list_members()

if __name__ == "__main__":
    main()
