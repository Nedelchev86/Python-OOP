from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Tihomir", 37, 50.50)
        self.player2 = TennisPlayer("Pavlin", 20, 60.00)

    def test_correct_initialization(self):
        self.assertEqual(self.player.name, "Tihomir")
        self.assertEqual(self.player.age, 37)
        self.assertEqual(self.player.points, 50.50)
        self.assertEqual(self.player.wins, [])

    def test_set_too_short_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "T"
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_set_too_short_name_two_char(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Tr"
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_low_than_ten(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 9
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_if_tournament_not_in_list(self):
        self.player.add_new_win("Bourgas")
        self.assertEqual(self.player.wins, ["Bourgas"])

    def test_add_new_win_with_tournament_in_list(self):
        self.player.wins.append("Bourgas")
        result = self.player.add_new_win("Bourgas")
        self.assertEqual(result, "Bourgas has been already added to the list of wins!")

    def test_first_player_with_less_points_than_secoond(self):
        result = self.player < self.player2
        self.assertEqual("Pavlin is a top seeded player and he/she is better than Tihomir", result)

    def test_first_player_with_more_points(self):
        self.player.points = 80.00
        result = self.player < self.player2
        self.assertEqual("Tihomir is a better player than Pavlin", result)

    def test_str_method(self):
        self.player.wins.append("Bourgas")
        self.player.wins.append("Varna")
        self.assertEqual("Tennis Player: Tihomir\n" \
               f"Age: 37\n" \
               f"Points: 50.5\n" \
               f"Tournaments won: Bourgas, Varna", str(self.player))


if __name__ == "__main__":
    main()