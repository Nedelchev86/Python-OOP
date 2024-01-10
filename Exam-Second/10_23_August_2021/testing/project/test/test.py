from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Bourgas")

    def test_correct_initialization(self):
        self.assertEqual(self.library.name, "Bourgas")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_if_author_not_in_books_by_author(self):
        self.library.add_book("Tihomir", "Python")
        self.assertEqual(self.library.books_by_authors["Tihomir"], ["Python"])

    def test_add_book_if_author_in_books_by_author(self):
        self.library.books_by_authors["Tihomir"] = ["Java"]
        self.library.add_book("Tihomir", "Python")
        self.assertEqual(self.library.books_by_authors["Tihomir"], ["Java", "Python"])

    def test_add_reader_not_in_readers(self):
        self.library.add_reader("Pesho")
        self.assertEqual(self.library.readers, {"Pesho": []})

    def test_add_Reader_already_added(self):
        self.library.readers = {"Pesho": []}
        result = self.library.add_reader("Pesho")
        self.assertEqual(result, "Pesho is already registered in the Bourgas library.")

    def test_rent_book_reader_not_in_readers(self):
        result = self.library.rent_book("Gosho", "Tihomir", "Python")
        self.assertEqual(result, "Gosho is not registered in the Bourgas Library.")

    def test_rent_book_with_no_such_author(self):
        self.library.readers = ["Gosho"]
        result = self.library.rent_book("Gosho", "Tihomir", "Python")
        self.assertEqual(result, "Bourgas Library does not have any Tihomir's books.")

    def test_rent_book_with_no_suck_book(self):
        self.library.readers = "Gosho"
        self.library.books_by_authors["Tihomir"] = ["Java"]
        result = self.library.rent_book("Gosho", "Tihomir", "Python")
        self.assertEqual(result, """Bourgas Library does not have Tihomir's "Python".""")

    def test_rent_success_book(self):
        self.library.readers = {"Gosho": []}
        self.library.books_by_authors["Tihomir"] = ["Java", "Python", "C++"]
        self.library.rent_book("Gosho", "Tihomir", "Python")
        self.assertEqual(self.library.readers["Gosho"], [{'Tihomir': 'Python'}])
        self.assertEqual(self.library.books_by_authors["Tihomir"], ["Java", "C++"])

        self.library.rent_book("Gosho", "Tihomir", "C++")
        self.assertEqual(self.library.readers["Gosho"], [{'Tihomir': 'Python'}, {'Tihomir': 'C++'}])
        self.assertEqual(self.library.books_by_authors["Tihomir"], ["Java"])






if __name__ == '__main__':
    main()