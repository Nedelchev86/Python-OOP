from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Tihomir", 34, 80.50)

    def test_correct_initialization(self):
        self.assertEqual(self.player.name, "Tihomir")
        self.assertEqual(self.player.age, 34)
        self.assertEqual(self.player.points, 80.50)
        self.assertEqual(self.player.wins, [])


    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Ko"
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_player_too_young(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 10
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_tournament(self):
        self.assertEqual(self.player.wins, [])
        self.player.add_new_win("Bourgas")
        self.assertEqual(self.player.wins, ["Bourgas"])

    def test_add_tournament_already_added(self):
        self.player.wins = ["Bourgas"]
        self.assertEqual(self.player.wins, ["Bourgas"])
        result = self.player.add_new_win("Bourgas")
        self.assertEqual(result, "Bourgas has been already added to the list of wins!")
        self.assertEqual(self.player.wins, ["Bourgas"])

    def test_lt_with_first_with_small_amount_of_points(self):
        player2 = TennisPlayer("Gosho", 20, 90.60)
        result = self.player < player2
        self.assertEqual(result, "Gosho is a top seeded player and he/she is better than Tihomir")

    def test_lt_with_first_with_bigger_amount_of_points(self):
        player2 = TennisPlayer("Gosho", 20, 50.60)
        result = self.player < player2
        self.assertEqual(result, "Tihomir is a better player than Gosho")

    def test_str_method(self):
        self.player.add_new_win("Bourgas")
        self.player.add_new_win("Sofia")
        result = f"Tennis Player: Tihomir\nAge: 34\nPoints: 80.5\nTournaments won: Bourgas, Sofia"
        self.assertEqual(result, str(self.player))


if __name__ == '__main__':
    main()