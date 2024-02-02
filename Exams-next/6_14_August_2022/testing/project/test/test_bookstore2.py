from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(3)
        self.bookstore2 = Bookstore(10)
        self.bookstore2.availability_in_store_by_book_titles = {"Test": 2, "Test2": 3}

    def test_correct_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 3)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_books_limit_with_zero_input(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(str(ve.exception), f"Books limit of 0 is not valid")

    def test_books_limit_with_negative_input(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        self.assertEqual(str(ve.exception), f"Books limit of -1 is not valid")

    def test_len_method(self):
        self.assertEqual(len(self.bookstore2), 5)

    def test_receive_book_when_not_enough_space(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.receive_book("Test3", 10)
        self.assertEqual(str(ex.exception),"Books limit is reached. Cannot receive more books!")

    def test_receive_book_if_book_not_in_dict(self):
        result = self.bookstore2.receive_book("Test3", 2)
        self.assertEqual(self.bookstore2.availability_in_store_by_book_titles["Test3"], 2)
        self.assertEqual(result, "2 copies of Test3 are available in the bookstore.")

    def test_receive_book_if_book_in_dict(self):
        result = self.bookstore2.receive_book("Test2", 2)
        self.assertEqual(self.bookstore2.availability_in_store_by_book_titles["Test2"], 5)
        self.assertEqual(result, "5 copies of Test2 are available in the bookstore.")

    def test_sell_book_if_book_not_in_dict(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.sell_book("Test4", 1)
        self.assertEqual(str(ex.exception), "Book Test4 doesn't exist!")

    def test_sell_book_in_dict_but_not_enough_copies(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.sell_book("Test", 4)
        self.assertEqual(str(ex.exception), "Test has not enough copies to sell. Left: 2")


    def test_sell_success(self):
        result = self.bookstore2.sell_book("Test", 1)
        self.assertEqual(self.bookstore2.availability_in_store_by_book_titles["Test"], 1)
        self.assertEqual(result, "Sold 1 copies of Test")
        self.assertEqual(self.bookstore2._Bookstore__total_sold_books, 1)
        self.assertEqual(self.bookstore2.availability_in_store_by_book_titles, {"Test": 1, "Test2": 3})

    def test_sell_success2(self):
        result = self.bookstore2.sell_book("Test", 2)
        self.assertEqual(self.bookstore2.availability_in_store_by_book_titles["Test"], 0)
        self.assertEqual(result, "Sold 2 copies of Test")
        self.assertEqual(self.bookstore2._Bookstore__total_sold_books, 2)

    def test_str_method(self):
        result = "Total sold books: 0\nCurrent availability: 5\n - Test: 2 copies\n - Test2: 3 copies"
        self.assertEqual(result, str(self.bookstore2))

if __name__ == '__main__':
    main()