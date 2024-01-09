from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(5)

    def test_bookstore_correct_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 5)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_total_sol_book(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_set_wrong_book_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(str(ve.exception), "Books limit of 0 is not valid")

    def test_set_negative_book_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -2
        self.assertEqual(str(ve.exception), "Books limit of -2 is not valid")

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        result = len(self.bookstore)
        self.assertEqual(result, 4)

    def test_len_method_with_zero(self):
        result = len(self.bookstore)
        self.assertEqual(result, 0)

    def test_receive_book_with_not_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Third", 3)

        self.assertEqual(len(self.bookstore), 4)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(len(self.bookstore), 4)

    def test_receive_book_with_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 1, "Second": 2}
        result = self.bookstore.receive_book("Third", 2)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 1, "Second": 2, "Third": 2})
        self.assertEqual(result, "2 copies of Third are available in the bookstore.")


    # def test_receive_book_book_title_not_in_books(self):
    #     self.bookstore.availability_in_store_by_book_titles = {'first': 1, 'second': 2}
    #
    #     result = self.bookstore.receive_book("random", 2)
    #
    #     self.assertEqual({'first': 1, 'second': 2, 'random': 2}, self.bookstore.availability_in_store_by_book_titles)
    #
    #     self.assertEqual(f"2 copies of random are available in the bookstore.", result)



    def test_receive_book_with_already_added_name(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        result = self.bookstore.receive_book("First", 1)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 3, "Second": 2})
        self.assertEqual(result, "3 copies of First are available in the bookstore.")

    # def test_receive_book_book_title_in_books(self):
    #     self.bookstore.availability_in_store_by_book_titles = {'first': 2, 'second': 1, 'third': 1}
    #
    #     result = self.bookstore.receive_book("first", 1)
    #
    #     self.assertEqual({'first': 3, 'second': 1, 'third': 1}, self.bookstore.availability_in_store_by_book_titles)
    #
    #     self.assertEqual(f"3 copies of first are available in the bookstore.", result)
    #
    #

    def test_sell_book_not_in_store(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 2, "Second": 2})
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Third", 1)
        self.assertEqual(str(ex.exception), "Book Third doesn't exist!")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 2, "Second": 2})

    def test_sell_book_with_available_name_but_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 2, "Second": 2})
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("First", 3)
        self.assertEqual(str(ex.exception), "First has not enough copies to sell. Left: 2")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 2, "Second": 2})

    def test_sell_book_with_available_name_and_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 2, "Second": 2})
        result = self.bookstore.sell_book("First", 2)
        self.assertEqual(result, "Sold 2 copies of First")
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {"First": 0, "Second": 2})
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["First"], 0)
        self.assertEqual(self.bookstore.total_sold_books, 2)

    def test_str_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.bookstore.sell_book("First", 1)
        result = "Total sold books: 1\nCurrent availability: 3\n - First: 1 copies\n - Second: 2 copies"
        self.assertEqual(result, str(self.bookstore))







if __name__ == "__main__":
    main()
