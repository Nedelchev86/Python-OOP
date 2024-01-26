from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual(self.toy.toy_shelf["A"], None)
        self.assertEqual(self.toy.toy_shelf["B"], None)
        self.assertEqual(self.toy.toy_shelf["C"], None)
        self.assertEqual(self.toy.toy_shelf["D"], None)
        self.assertEqual(self.toy.toy_shelf["E"], None)
        self.assertEqual(self.toy.toy_shelf["F"], None)
        self.assertEqual(self.toy.toy_shelf["G"], None)

    def test_add_toy_in_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("W", "Bear")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_in_wrong_correct_name_but_already_added_same_toy(self):
        self.toy.toy_shelf["A"] = "Bear"
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Bear")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_in_wrong_correct_name_but_is_taken(self):
        self.toy.toy_shelf["A"] = "Bear"
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Lion")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_with_success(self):
        result = self.toy.add_toy("A", "Bear")
        self.assertEqual(result, "Toy:Bear placed successfully!")
        self.assertEqual(self.toy.toy_shelf["A"], "Bear")

    def test_remove_with_wrong_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("W", "Bear")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toys_with_other_toy_name_in_shelf(self):
        result = self.toy.add_toy("A", "Bear")
        with self.assertRaises(Exception) as ex:
            result = self.toy.remove_toy("A", "Lion")
        self.assertEqual(str(ex.exception), ("Toy in that shelf doesn't exists!"))

    def test_remove_toys_success(self):
        self.toy.toy_shelf["A"] = "Bear"
        result = self.toy.remove_toy("A", "Bear")
        self.assertEqual(result, "Remove toy:Bear successfully!")
        self.assertEqual(self.toy.toy_shelf["A"], None)

if __name__ == '__main__':
    main()