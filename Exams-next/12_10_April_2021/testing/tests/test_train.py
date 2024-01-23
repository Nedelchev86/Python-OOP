from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 5)

    def test_initialization(self):
        self.assertEqual(self.train.name, "Test")
        self.assertEqual(self.train.capacity, 5)
        self.assertEqual(self.train.passengers , [])

    def test_add_method_with_no_capacity(self):
        self.train.passengers = ["test1", "test2", "test3", "test4", "test5"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("test6")
        self.assertEqual(str(ve.exception), "Train is full")

    def test_add_method_with_enough_capacity_but_name_in_list(self):
        self.train.passengers = ["test1", "test2", "test3"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("test2")
        self.assertEqual(str(ve.exception),  "Passenger test2 Exists")
        self.assertEqual(self.train.passengers, ["test1", "test2", "test3"])

    def test_add_method_with_enough_capacity_and_name_not_in_list(self):
        self.train.passengers = ["test1", "test2", "test3"]
        result = self.train.add("test4")
        self.assertEqual(result,  "Added passenger test4")
        self.assertEqual(self.train.passengers, ["test1", "test2", "test3", "test4"])

    def test_remove_if_passenger_not_in_list(self):
        self.train.passengers = ["test1", "test2", "test3"]
        with self.assertRaises(ValueError) as ve:
            self.train.remove("test4")
        self.assertEqual(str(ve.exception), "Passenger Not Found")
        self.assertEqual(self.train.passengers, ["test1", "test2", "test3"])

    def test_remove_if_passenger_in_list(self):
        self.train.passengers = ["test1", "test2", "test3"]
        result = self.train.remove("test2")
        self.assertEqual(result, "Removed test2")
        self.assertEqual(self.train.passengers, ["test1", "test3"])

if __name__ == '__main__':
    main()