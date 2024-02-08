from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Silo", 2223, 9.5)
        self.movie.actors = ["Tihomir", "Pavlin"]
        self.movie2 = Movie("Test", 2222, 9.0)


    def test_correct_initialization(self):
        self.assertEqual(self.movie.name, "Silo")
        self.assertEqual(self.movie.year, 2223)
        self.assertEqual(self.movie.rating, 9.5)
        self.assertEqual(self.movie.actors, ["Tihomir", "Pavlin"])

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_already_added(self):
        result = self.movie.add_actor("Tihomir")
        self.assertEqual(result, "Tihomir is already added in the list of actors!")

    def test_add_actor_not_in_list(self):
        self.movie.add_actor("Ivan")
        self.assertEqual(self.movie.actors, ["Tihomir", "Pavlin", "Ivan"])

    def test_gt_method_with_first_greater(self):
        result = self.movie > self.movie2
        self.assertEqual(result, '"Silo" is better than "Test"')

    def test_gt_method_with_second_greater(self):
        self.movie.rating = 8.0
        result = self.movie > self.movie2
        self.assertEqual(result, '"Test" is better than "Silo"')

    def test_repr_method(self):
        result = "Name: Silo\nYear of Release: 2223\nRating: 9.50\nCast: Tihomir, Pavlin"
        self.assertEqual(result, repr(self.movie))




if __name__ == '__main__':
    main()