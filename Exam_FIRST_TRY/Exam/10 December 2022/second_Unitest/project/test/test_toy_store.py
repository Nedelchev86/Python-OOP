from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toys = ToyStore()

    def test_initialization(self):
        self.assertEqual(None, self.toys.toy_shelf["A"])
        self.assertEqual(None, self.toys.toy_shelf["B"])
        self.assertEqual(None, self.toys.toy_shelf["C"])
        self.assertEqual(None, self.toys.toy_shelf["D"])
        self.assertEqual(None, self.toys.toy_shelf["E"])
        self.assertEqual(None, self.toys.toy_shelf["F"])
        self.assertEqual(None, self.toys.toy_shelf["G"])

    def test_add_toy_if_not_in_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("V", "Ivan")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_toys_already_in_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("A", None)
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_toys_already_in_shelf_but_is_taken_raise_exception(self):
        self.toys.add_toy("A", "Barbie")
        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("A", "Brar")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_if_toys_already_in_shelf_but_not_taken_raise_exception(self):

        result = self.toys.add_toy("A", "Barbie")
        self.assertEqual(self.toys.toy_shelf["A"], "Barbie")
        self.assertEqual("Toy:Barbie placed successfully!", result)

    def test_remove_toy_if_toy_not_in_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toys.remove_toy("V", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_toy_is_in_shelf_but_with_other_name(self):
        self.toys.toy_shelf["A"] = "Barbie"
        with self.assertRaises(Exception) as ex:
            self.toys.remove_toy("A", "Bear")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_with_correct_key_and_none_value(self):
        self.toys.toy_shelf["A"] = "Barbie"
        result = self.toys.remove_toy("A", "Barbie")
        self.assertEqual(self.toys.toy_shelf["A"], None)
        self.assertEqual("Remove toy:Barbie successfully!", result)


if __name__ == '__main__':
    main()