from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("KVS")

    def test_correct_initialization(self):
        self.assertEqual(self.team.name, "KVS")
        self.assertEqual(self.team.members, {})

    def test_set_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Bad name"
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        result = self.team.add_member(**{"Tihomir": 24, "Georgi": 33, "Ivan": 11})
        self.assertEqual(result, "Successfully added: Tihomir, Georgi, Ivan")
        self.assertEqual(self.team.members,{"Tihomir": 24, "Georgi": 33, "Ivan": 11})

    def test_add_player_already_Added(self):
        self.team.members = {"Tihomir": 22}
        result = self.team.add_member(**{"Tihomir": 24})
        self.assertEqual(result, "Successfully added: ")
        self.assertEqual(self.team.members,{"Tihomir": 22})

    def test_del_name_not_added(self):
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        result = self.team.remove_member("Gosho")
        self.assertEqual(result, "Member with name Gosho does not exist")

    def test_del_name_in_list(self):
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        result = self.team.remove_member("Georgi")
        self.assertEqual(result, "Member Georgi removed")
        self.assertEqual(self.team.members, {"Tihomir": 24, "Ivan": 11})

    def test_gt_with_first(self):
        team2 = Team("Chernomorets")
        team2.members = {"Test": 11, "Test2": 22}
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        result = self.team > team2
        self.assertTrue(self.team > team2)
        self.assertEqual(result, True)

    def test_gt_with_second(self):
        team2 = Team("Chernomorets")
        team2.members = {"Test": 11, "Test2": 22, "Test3": 12, "Test4": 33}
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        result = self.team > team2
        self.assertFalse(self.team > team2)
        self.assertEqual(result, False)

    def test_len(self):
        team2 = Team("Chernomorets")
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        self.assertEqual(len(self.team), 3)
        self.assertEqual(len(team2), 0)

    def test_add(self):
        team2 = Team("Chernomorets")
        team2.members = {"Test": 11, "Test2": 22}
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        new_team = self.team + team2
        self.assertEqual(new_team.name, "KVSChernomorets")
        self.assertEqual(new_team.members, {"Test": 11, "Test2": 22, "Tihomir": 24, "Georgi": 33, "Ivan": 11})

    def test_str(self):
        self.team.members = {"Tihomir": 24, "Georgi": 33, "Ivan": 11}
        result = "Team name: KVS\nMember: Georgi - 33-years old\nMember: Tihomir - 24-years old\nMember: Ivan - 11-years old"
        self.assertEqual(str(self.team), result)
