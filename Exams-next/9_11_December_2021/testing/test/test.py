from project.team import Team
from unittest import TestCase, main


class TestTests(TestCase):
    def setUp(self):
        self.team = Team("Python")
        self.team.members = {"Tihomir": 37, "Pavlin": 12}

        self.team2 = Team("JavaScript")
        self.team2.members = {"Ivan": 10}

    def test_correct_initialization(self):
        self.assertEqual(self.team.name, "Python")
        self.assertEqual(self.team.members, {"Tihomir": 37, "Pavlin": 12})

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Bad Name"
        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):

        result = self.team.add_member(Gosho=22, Pesho=25, Tihomir=22)
        added_members_by_name = ["Gosho", "Pesho"]


        self.assertEqual(self.team.members["Gosho"], 22)
        self.assertEqual(self.team.members["Pesho"], 25)
        self.assertEqual(self.team.members["Tihomir"], 37)
        self.assertEqual(result, "Successfully added: Gosho, Pesho")
        self.assertEqual(added_members_by_name, ["Gosho", "Pesho"])
        self.assertEqual(self.team.members, {"Tihomir": 37, "Pavlin": 12, "Gosho": 22, "Pesho": 25})


    def test_remove_member_in_list(self):
        result = self.team.remove_member("Tihomir")
        self.assertEqual(result, "Member Tihomir removed")
        self.assertEqual(self.team.members, {"Pavlin": 12})

    def test_remove_member_not_in_list(self):
        result = self.team.remove_member("Ivan")
        self.assertEqual(result, "Member with name Ivan does not exist")
        self.assertEqual(self.team.members, {"Tihomir": 37, "Pavlin": 12})

    def test_gt_method(self):
        result= self.team > self.team2
        self.assertEqual(result, True)

    def test_gt_method2(self):
        self.team.members = {}
        result = self.team > self.team
        self.assertEqual(result, False)

    def test_len(self):
        self.team2.members = {}
        self.assertEqual(len(self.team), 2)
        self.assertEqual(len(self.team2), 0)

    def test_add_method(self):
        new_team = self.team + self.team2
        self.assertEqual(new_team.name, "PythonJavaScript")
        self.assertEqual(new_team.members, {"Tihomir": 37, "Pavlin": 12, "Ivan": 10})

    def test_str_method(self):
        result = "Team name: Python\nMember: Tihomir - 37-years old\nMember: Pavlin - 12-years old"
        self.assertEqual(result, str(self.team))


if __name__ == "__main__":
    main()