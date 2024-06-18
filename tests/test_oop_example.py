import sys
import os
import unittest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from oop_example import Book, Member, Library

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.library = Library()

        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
        self.book2 = Book("1984", "George Orwell", "0987654321")

        self.member1 = Member("Alice", "M001")
        self.member2 = Member("Bob", "M002")

        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        self.library.register_member(self.member1)
        self.library.register_member(self.member2)

    def test_add_book(self):
        book3 = Book("To Kill a Mockingbird", "Harper Lee", "1122334455")
        self.library.add_book(book3)
        self.assertIn("1122334455", self.library.books)

    def test_register_member(self):
        member3 = Member("Charlie", "M003")
        self.library.register_member(member3)
        self.assertIn("M003", self.library.members)

    def test_check_out_book(self):
        self.library.check_out_book("1234567890", "M001")
        self.assertTrue(self.book1.is_checked_out)
        self.assertIn(self.book1, self.member1.checked_out_books)

    def test_return_book(self):
        self.library.check_out_book("1234567890", "M001")
        self.library.return_book("1234567890", "M001")
        self.assertFalse(self.book1.is_checked_out)
        self.assertNotIn(self.book1, self.member1.checked_out_books)

    def test_list_books(self):
        with self.assertLogs(level='INFO') as cm:
            self.library.list_books()
        self.assertIn("The Great Gatsby by F. Scott Fitzgerald (ISBN: 1234567890)", cm.output[0])

    def test_list_members(self):
        with self.assertLogs(level='INFO') as cm:
            self.library.list_members()
        self.assertIn("Member: Alice, ID: M001", cm.output[0])

if __name__ == "__main__":
    unittest.main()
