from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_initialization(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -4
        self.assertEqual(str(ve.exception),"Size must be positive number!")

    def test_hire_worker_with_worker_already_in_list(self):
        self.plantation.workers.append("Ivan")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_with_worker_noy_in_list(self):
        result = self.plantation.hire_worker("Ivan")
        result2 = self.plantation.hire_worker("Pesho")
        self.assertEqual("Ivan successfully hired.", result)
        self.assertEqual("Pesho successfully hired.", result2)
        self.assertEqual(self.plantation.workers, ["Ivan", "Pesho"])

    def test_len_method(self):
        self.plantation.workers= ["Ivan", "Pesho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        result = len(self.plantation)
        self.assertEqual(result, 3)

    def test_planting_with_wrong_worker_raise_exception(self):
        self.plantation.workers = ["Ivan", "Pesho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "apples")
        self.assertEqual("Worker with name Gosho is not hired!", str(ve.exception))

    def test_planting_with_valid_worker_but_not_enough_space_raise_exception(self):
        self.plantation.size = 3
        self.plantation.workers = ["Ivan", "Pesho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "bananas")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_valid_worker_and_have_enough_space_raise_exception(self):
        self.plantation.workers = ["Ivan", "Pesho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        result = self.plantation.planting("Ivan", "bananas")
        self.assertEqual(result, "Ivan planted bananas.")
        self.assertEqual(self.plantation.plants["Ivan"], ["flowers", "bananas"])

    def test_planting_with_valid_worker_and_have_enough_space(self):
        self.plantation.workers = ["Ivan", "Pesho", "Gosho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        result = self.plantation.planting("Gosho", "bananas")
        self.assertEqual(result, "Gosho planted it's first bananas.")
        self.assertEqual(self.plantation.plants["Gosho"], ["bananas"])

    def test_str_method(self):
        self.plantation.workers = ["Ivan", "Pesho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        self.assertEqual("Plantation size: 10\nIvan, Pesho\nIvan planted: flowers\nPesho planted: apples, strawberries", str(self.plantation))

    def test_repr_method(self):
        self.plantation.workers = ["Ivan", "Pesho"]
        self.plantation.plants = {"Ivan": ["flowers"], "Pesho": ["apples", "strawberries"]}
        self.assertEqual(self.plantation.__repr__(), "Size: 10\nWorkers: Ivan, Pesho")



if __name__ == "__main__":
    main()
