
from project.tennis_player import TennisPlayer
import unittest

class TestTennisPlayer(unittest.TestCase):
    #  Tests that a TennisPlayer object can be created with valid name, age and points
    def test_create_tennis_player_with_valid_data(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.name, 'John Doe')
        self.assertEqual(player.age, 20)
        self.assertEqual(player.points, 100.0)
        self.assertEqual(player.wins, [])

    #  Tests that a new win can be added to the TennisPlayer's list of wins
    def test_add_new_win_to_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.add_new_win('Wimbledon'), None)
        self.assertEqual(player.wins, ['Wimbledon'])
        self.assertEqual(player.add_new_win('Wimbledon'), 'Wimbledon has been already added to the list of wins!')
        self.assertEqual(player.wins, ['Wimbledon'])

    #  Tests that two TennisPlayer objects can be compared based on their points
    def test_compare_two_tennis_players_based_on_points(self):
        player1 = TennisPlayer('John Doe', 20, 100.0)
        player2 = TennisPlayer('Jane Doe', 22, 200.0)
        self.assertLess(player1, player2)
        self.assertEqual(player2 < player1, f'{player1.name} is a top seeded player and he/she is better than {player2.name}')
        self.assertEqual(player1 < player2, f'{player2.name} is a better player than {player1.name}')

    #  Tests that a TennisPlayer object cannot be created with a name less than 3 characters
    def test_create_tennis_player_with_name_less_than_3_characters(self):
        with self.assertRaises(ValueError):
            TennisPlayer('Jo', 20, 100.0)

    #  Tests that a TennisPlayer object cannot be created with an age less than 18
    def test_create_tennis_player_with_age_less_than_18(self):
        with self.assertRaises(ValueError):
            TennisPlayer('John Doe', 16, 100.0)

    #  Tests that a tournament cannot be added to the TennisPlayer's list of wins if it has already been added
    def test_add_tournament_to_tennis_player_wins_that_has_already_been_added(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        player.add_new_win('Wimbledon')
        self.assertEqual(player.add_new_win('Wimbledon'), 'Wimbledon has been already added to the list of wins!')
        self.assertEqual(player.wins, ['Wimbledon'])

    #  Tests that the name of a TennisPlayer object can be retrieved
    def test_get_name_of_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.name, 'John Doe')

    #  Tests that the age of a TennisPlayer object can be retrieved
    def test_get_age_of_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.age, 20)

    #  Tests that the points of a TennisPlayer object can be retrieved
    def test_get_points_of_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.points, 100.0)

    #  Tests that the list of wins of a TennisPlayer object can be retrieved
    def test_get_list_of_wins_of_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        self.assertEqual(player.wins, [])

    #  Tests that the name of a TennisPlayer object can be set
    def test_set_name_of_tennis_player(self):
        player = TennisPlayer('John Doe', 20, 100.0)
        player.name = 'Jane Doe'
        self.assertEqual(player.name, 'Jane Doe')

    #  Tests that two TennisPlayer objects with equal points are considered equal
    def test_tennis_player_comparison_with_equal_points(self):
        player1 = TennisPlayer('John Doe', 20, 100.0)
        player2 = TennisPlayer('Jane Doe', 22, 100.0)
        self.assertEqual(player1, player2)
        self.assertEqual(player2, player1)
