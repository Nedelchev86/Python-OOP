from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(4)
    
    def test_initialization(self):
        self.assertEqual(4, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)
        self.assertEqual(self.store._Bookstore__total_sold_books, 0)

    def test_total_sol_book(self):
        self.assertEqual(0, self.store.total_sold_books)

    def test_book_limit_with_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -3
        self.assertEqual("Books limit of -3 is not valid", str(ve.exception))

    def test_book_limit_with_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_len_method(self):
        result = len(self.store)
        self.assertEqual(0, result)

    def test_len_method_with_books(self):
        self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
        result = len(self.store)
        self.assertEqual(3, result)

    # def test_receive_book_with_not_enough_space(self):
    #     self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 2})
    #     self.assertEqual(len(self.store), 3)
    #     with self.assertRaises(Exception) as ex:
    #         self.store.receive_book("C++", 4)
    #     self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 2})
    #     self.assertEqual(len(self.store), 3)

    def test_receive_book_with_not_enough_space(self):
        self.store.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Third", 3)

        self.assertEqual(len(self.store), 4)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")
        self.store.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(len(self.store), 4)

    # def test_receive_book_with_not_enough_space2(self):
    #     self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 2})
    #     result = self.store.receive_book("C++", 1)
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 2, "C++": 1})
    #     self.assertEqual("1 copies of C++ are available in the bookstore.", result)

    def test_receive_book_with_enough_space(self):
        self.store.availability_in_store_by_book_titles = {"First": 1, "Second": 2}
        result = self.store.receive_book("Third", 1)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"First": 1, "Second": 2, "Third": 1})
        self.assertEqual(result, "1 copies of Third are available in the bookstore.")



    # def test_receive_book_with_not_enough_space3(self):
    #     self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 2})
    #     self.assertEqual(2, self.store.availability_in_store_by_book_titles["Python"])
    #     result = self.store.receive_book("Python", 1)
    #     self.assertEqual(self.store.availability_in_store_by_book_titles, {"Java": 1, "Python": 3})
    #     self.assertEqual("3 copies of Python are available in the bookstore.", result)
    #     self.assertEqual(3, self.store.availability_in_store_by_book_titles["Python"])

    def test_receive_book_with_already_added_name(self):
        self.store.availability_in_store_by_book_titles = {"First": 1, "Second": 1}
        result = self.store.receive_book("First", 1)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"First": 2, "Second": 1})
        self.assertEqual(result, "2 copies of First are available in the bookstore.")


    # def test_sell_book_not_in_store(self):
    #     self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
    #     with self.assertRaises(Exception) as ex:
    #         self.store.sell_book("Gosho", 2)
    #     self.assertEqual("Book Gosho doesn't exist!", str(ex.exception))

    def test_sell_book_not_in_store(self):
        self.store.availability_in_store_by_book_titles = {"First": 2, "Second": 2}
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"First": 2, "Second": 2})
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Third", 1)
        self.assertEqual(str(ex.exception), "Book Third doesn't exist!")
        self.assertEqual(self.store.availability_in_store_by_book_titles, {"First": 2, "Second": 2})


    def test_sell_book_in_Store_but_not_enough_copies(self):
        self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
        self.assertEqual(self.store.total_sold_books, 0)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Python", 3)
        self.assertEqual(self.store.total_sold_books, 0)
        self.assertEqual("Python has not enough copies to sell. Left: 2", str(ex.exception))

    def test_succesiful_sell_book(self):
        self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
        self.assertEqual(self.store.availability_in_store_by_book_titles["Python"], 2)
        self.assertEqual(self.store.total_sold_books, 0)
        result =   self.store.sell_book("Python", 1)
        self.assertEqual("Sold 1 copies of Python", result)
        self.assertEqual(self.store.availability_in_store_by_book_titles["Python"], 1)
        self.assertEqual(self.store.total_sold_books, 1)

    def test_succesiful_sell_book2(self):
        self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
        self.assertEqual(self.store.availability_in_store_by_book_titles["Python"], 2)
        self.assertEqual(self.store.total_sold_books, 0)
        result =   self.store.sell_book("Python", 2)
        self.assertEqual("Sold 2 copies of Python", result)
        self.assertEqual(self.store.availability_in_store_by_book_titles["Python"], 0)
        self.assertEqual(self.store.total_sold_books, 2)

    def test_str_method(self):
        self.store.availability_in_store_by_book_titles = {"Java": 1, "Python": 2}
        result = "Total sold books: 0\nCurrent availability: 3\n - Java: 1 copies\n - Python: 2 copies"
        self.assertEqual(result , str(self.store))

    def test_str_method_With_no_bool(self):
        result = "Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(result, str(self.store))



if __name__ == '__main__':
    main()
