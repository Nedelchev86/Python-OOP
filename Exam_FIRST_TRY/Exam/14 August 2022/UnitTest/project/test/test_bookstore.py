from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(4)

    def test_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 4)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_total_sold_books(self):
        result = self.bookstore.total_sold_books
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, result)

    def test_book_limit_setter_with_zero_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 3}
        result = len(self.bookstore)
        self.assertEqual(result, 5)

    def test_receive_book_over_the_book_limit(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Some Book", 10)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receice_book_with_enough_space_and_book_not_in_store(self):
        self.bookstore.receive_book("Some Book", 1)
        self.bookstore.receive_book("Some Book2", 2)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["Some Book"], 1)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["Some Book2"], 2)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"Some Book": 1, "Some Book2": 2})

    def test_receice_book_with_enough_space_and_book_not_in_store_test_Return(self):
        self.bookstore.receive_book("Some Book", 1)
        result = self.bookstore.receive_book("Some Book", 2)
        self.assertEqual(result, "3 copies of Some Book are available in the bookstore.")

    def test_sell_book_if_book_not_in_store_raises_exception(self):
        self.bookstore.receive_book("Some Book", 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Some Book2", 1)
        self.assertEqual("Book Some Book2 doesn't exist!", str(ex.exception))

    def test_sell_book_if_book_is_in_store_but_not_enough_copies(self):
        self.bookstore.receive_book("Some Book", 3)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Some Book", 4)
        self.assertEqual("Some Book has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_which_is_in_store_and_have_enough_copies(self):
        self.bookstore.receive_book("Some Book", 4)
        result = self.bookstore.sell_book("Some Book", 3)
        self.assertEqual(result, "Sold 3 copies of Some Book")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["Some Book"], 1)
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 3)
        self.assertEqual(len(self.bookstore), 1)
        result = self.bookstore.sell_book("Some Book", 1)
        self.assertEqual(result, "Sold 1 copies of Some Book")

    def test_str(self):
        self.bookstore.receive_book("Some Book", 2)
        self.bookstore.receive_book("Some Book2", 1)
        result = str(self.bookstore)
        self.assertEqual("Total sold books: 0\nCurrent availability: 3\n - Some Book: 2 copies\n - Some Book2: 1 copies", result)


if __name__ == "__main__":
    main()