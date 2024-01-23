from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Miladinovi")
        self.library.books_by_authors = {"Pesho": ["Test1", "Test2"]}

    def test_correct_initialization(self):
        self.assertEqual(self.library.name, "Miladinovi")
        self.assertEqual(self.library.books_by_authors, {"Pesho": ["Test1", "Test2"]})
        self.assertEqual(self.library.readers, {})

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    # def test_add_book_with_author_not_in_dict(self):
    #     self.assertEqual(self.library.books_by_authors, {"Pesho": ["Test1", "Test2"]})
    #     self.library.add_book("Gosho", "Test4")
    #     self.assertEqual(self.library.books_by_authors, {"Pesho": ["Test1", "Test2"], "Gosho": ["Test4"]})
    #     self.assertEqual(self.library.books_by_authors["Gosho"], ["Test4"])
    def test_successful_add_book_in_dict_new_author(self):
        self.library.books_by_authors = {}
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Joro", "Joro World")

        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

        self.library.add_book("Joro1", "Joro World")

        self.assertEqual({"Joro": ["Joro World"], "Joro1": ["Joro World"]}, self.library.books_by_authors)



    # def test_add_book_with_author_in_list_but_book_not_in_list(self):
    #     self.library.add_book("Pesho", "Test3")
    #     self.assertEqual(self.library.books_by_authors, {"Pesho": ["Test1", "Test2", "Test3"]})
    #     self.assertEqual(self.library.books_by_authors["Pesho"], ["Test1", "Test2", "Test3"])

    def test_successful_add_book_in_dict_new_title(self):
        self.library.books_by_authors = {}
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Joro", "Joro World")
        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

        self.library.add_book("Joro", "Joro World 2")
        self.assertEqual({"Joro": ["Joro World", "Joro World 2"]}, self.library.books_by_authors)


    def test_add_reader_with_reader_not_in_list(self):
        self.library.readers = {"Ivan": []}
        self.library.add_reader("Tihomir")
        self.assertEqual(self.library.readers, {"Ivan": [], "Tihomir": []})

    # def test_add_reader_already_Added(self):
    #     self.library.readers = {"Ivan": [], "Tihomir": []}
    #     result = self.library.add_reader("Tihomir")
    #     self.assertEqual(result, "Tihomir is already registered in the Miladinovi library.")
    #     self.assertEqual(self.library.readers, {"Ivan": [], "Tihomir": []})

    def test_unsuccessful_add_reader_return_duplicity_message(self):
        self.library.add_reader("Joro")
        result = self.library.add_reader("Joro")

        self.assertEqual("Joro is already registered in the Miladinovi library.", result)
        self.assertTrue("Joro" in self.library.readers)

    def test_rent_book_with_reader_not_in_list(self):
        self.library.readers = {"Ivan": []}
        result = self.library.rent_book("Tihomir", "Pesho", "Test1")
        self.assertEqual(result, "Tihomir is not registered in the Miladinovi Library.")
        self.assertEqual(self.library.readers, {'Ivan': []})
        self.assertEqual(self.library.books_by_authors, {'Pesho': ['Test1', 'Test2']})

    def test_rent_book_with_wrong_author(self):
        self.library.readers = {"Tihomir": []}
        result = self.library.rent_book("Tihomir", "Gosho", "Test1")
        self.assertEqual(result, "Miladinovi Library does not have any Gosho's books.")

    def test_rent_book_not_in_books(self):
        self.library.readers = {"Tihomir": []}
        result = self.library.rent_book("Tihomir", "Pesho", "Test3")
        self.assertEqual(result, 'Miladinovi Library does not have Pesho\'s "Test3".')
        self.assertEqual(self.library.books_by_authors["Pesho"], ['Test1', 'Test2'])

    def test_rent_book_with_all_correct_data(self):
        self.library.readers = {"Tihomir": []}
        self.library.rent_book("Tihomir", "Pesho", "Test2")
        self.assertEqual(self.library.readers["Tihomir"], [{"Pesho": "Test2"}])
        self.assertEqual(self.library.readers, {'Tihomir': [{'Pesho': 'Test2'}]})
        self.assertEqual(self.library.books_by_authors, {'Pesho': ['Test1']})


if __name__ == '__main__':
    main()