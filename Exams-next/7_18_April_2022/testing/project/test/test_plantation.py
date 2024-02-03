from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(4)
        self.plantation2 = Plantation(5)
        self.plantation2.workers.append("Tihomir")
        self.plantation2.plants = {"Tihomir": ["Roses"]}


    def test_correct_initialization(self):
        self.assertEqual(self.plantation.size, 4)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker_than_already_hires(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation2.hire_worker("Tihomir")
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_new_worker(self):
        result = self.plantation2.hire_worker("Ivan")
        self.assertEqual(result, "Ivan successfully hired.")
        self.assertEqual(self.plantation2.workers, ["Tihomir", "Ivan"])

    def test_len_method(self):
        self.assertEqual(len(self.plantation2), 1)

    def test_len_method2(self):
        self.assertEqual(len(self.plantation), 0)

    def test_len_method3(self):
        self.plantation.workers.append("Ivan")
        self.plantation.plants = {"Tihomir": ["Test", "Test2"], "Ivan": ["Test4", "Test5"]}
        self.assertEqual(len(self.plantation), 4)

    def test_planting_with_wrong_workers(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation2.planting("Ivan", "Weed")
        self.assertEqual(str(ve.exception), "Worker with name Ivan is not hired!")

    def test_planting_with_not_enough_size(self):
        self.plantation2.size = 1
        with self.assertRaises(ValueError) as ve:
            self.plantation2.planting("Tihomir", "Weed")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_with_not_enough_size2(self):
        self.plantation2.size = 1
        self.plantation2.plants = {"Tihomir": ["Test, Test, Test3"]}
        with self.assertRaises(ValueError) as ve:
            self.plantation2.planting("Tihomir", "Weed")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_with_plants_in_plants(self):
        result = self.plantation2.planting("Tihomir", "Weed")
        self.assertEqual(result, "Tihomir planted Weed.")
        self.assertEqual(self.plantation2.plants["Tihomir"], ["Roses", "Weed"])

    def test_planting_with_not_same_worker_in_plants(self):
        self.plantation2.workers.append("Ivan")
        result = self.plantation2.planting("Ivan", "Weed")
        self.assertEqual(result, "Ivan planted it's first Weed.")
        self.assertEqual(self.plantation2.plants["Ivan"], ["Weed"])

    def test_str_method(self):
        self.plantation2.workers.append("Ivan")
        result = "Plantation size: 5\nTihomir, Ivan\nTihomir planted: Roses"
        self.assertEqual(result, str(self.plantation2))

    def test_repr_method(self):
        self.plantation2.workers.append("Ivan")
        result = "Size: 5\nWorkers: Tihomir, Ivan"
        self.assertEqual(result, repr(self.plantation2))




if __name__ == '__main__':
    main()