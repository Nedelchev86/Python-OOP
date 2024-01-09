from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Silo", 2023, 9.5)

    def test_correct_initialization(self):
        self.assertEqual(self.movie.name, "Silo")
        self.assertEqual(self.movie.year, 2023)
        self.assertEqual(self.movie.rating, 9.5)
        self.assertEqual(self.movie.actors, [])

    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_wrong_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_Actor_already_added(self):
        self.movie.actors.append("Tihomir")
        result = self.movie.add_actor("Tihomir")
        self.assertEqual(result, "Tihomir is already added in the list of actors!")

    def test_add_new_actor(self):
        self.movie.actors.append("Tihomir")
        self.assertEqual(self.movie.actors, ["Tihomir"])
        self.movie.add_actor("Pavlin")
        self.assertEqual(self.movie.actors, ["Tihomir", "Pavlin"])

    def test_tt_method_with_first_greater_rating(self):
        other = Movie("The Lord of the Rings", 2014, 9.0)
        result = self.movie > other
        self.assertEqual(result, '"Silo" is better than "The Lord of the Rings"')

    def test_tt_method_with_second_greater_rating(self):
        other = Movie("The Lord of the Rings", 2014, 10)
        result = self.movie > other
        self.assertEqual(result, '"The Lord of the Rings" is better than "Silo"')

    def test_repr_method(self):
        self.movie.actors = ["Tihomir", "Pavlin"]
        result = "Name: Silo\nYear of Release: 2023\nRating: 9.50\nCast: Tihomir, Pavlin"
        self.assertEqual(result, repr(self.movie))



if __name__ == '__main__':
    main()