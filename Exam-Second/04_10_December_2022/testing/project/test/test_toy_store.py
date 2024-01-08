from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_initialization(self):
        self.assertEqual(self.store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_not_correct_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("W", "Bear")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_already_added(self):
        self.store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Bear")
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_un_taken_shelf(self):
        self.store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Dog")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_success_toy(self):
        result = self.store.add_toy("A", "Bear")
        self.assertEqual(result, "Toy:Bear placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "Bear")

    def test_remove_toy_not_correct_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("W", "Bear")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_already_added(self):
        self.store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Dog")
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_success(self):
        self.store.toy_shelf["A"] = "Bear"
        result = self.store.remove_toy("A", "Bear")
        self.assertEqual(result, "Remove toy:Bear successfully!")
        self.assertEqual(self.store.toy_shelf["A"], None)



if __name__ == '__main__':
    main()