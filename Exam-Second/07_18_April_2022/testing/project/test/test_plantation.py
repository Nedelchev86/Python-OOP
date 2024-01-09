from project.plantation import Plantation
from unittest import  TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_correct_initialization(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_set_size_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_workers_already_hared(self):
        self.plantation.workers.append("Tisho")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Tisho")
        self.assertEqual(str(ve.exception), "Worker already hired!")

    def test_hire_workers(self):
        self.plantation.workers.append("Gosho")
        result = self.plantation.hire_worker("Tisho")
        self.assertEqual(result, "Tisho successfully hired.")
        self.assertEqual(self.plantation.workers, ["Gosho", "Tisho"])

    def test_len_method(self):
        self.assertEqual(len(self.plantation), 0)

    def test_len_method_with_plants(self):
        self.plantation.hire_worker("Tisho")
        self.plantation.plants = {"Tisho": ["Roses", "Flowers"]}
        self.assertEqual(len(self.plantation), 2)

    def test_planting_with_worker_not_hiredd(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Tisho", "Flowers")
        self.assertEqual(str(ve.exception), "Worker with name Tisho is not hired!")
        self.assertEqual(self.plantation.plants, {})

    def test_planting_with_correct_worker_but_not_enough_space(self):
        self.plantation.workers = ["Tisho", "Gosho"]
        self.plantation.plants = {"Tisho": ["Test1","Test2","Test3","Test4","Test5","Test6"], "Gosho": ["Test7","Test8","Test9","Test10",]}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Tisho", "Roses")
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planting_with_correct_data(self):
        self.plantation.workers = ["Tisho"]
        self.plantation.plants = {"Tisho": ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6"]}
        result = self.plantation.planting("Tisho", "Test7")
        self.assertEqual(result , f"Tisho planted Test7.")
        self.assertEqual(self.plantation.plants, {"Tisho": ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7"]})

    def test_planting_with_correct_new_data(self):
        self.plantation.workers = ["Tisho", "Gosho"]
        self.plantation.plants = {"Tisho": ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6"]}
        result = self.plantation.planting("Gosho", "Test7")
        self.assertEqual(result , f"Gosho planted it's first Test7.")
        self.assertEqual(self.plantation.plants["Gosho"], ["Test7"])

    def test_str(self):
        self.plantation.workers = ["Tisho", "Gosho"]
        self.plantation.plants = {"Tisho": ["Test1", "Test2"],
                                  "Gosho": ["Test7", "Test8"]}
        result = "Plantation size: 10\nTisho, Gosho\nTisho planted: Test1, Test2\nGosho planted: Test7, Test8"
        self.assertEqual(result, str(self.plantation))

    def test_repr(self):
        self.plantation.workers = ["Tisho", "Gosho"]
        self.plantation.plants = {"Tisho": ["Test1", "Test2"],
                                  "Gosho": ["Test7", "Test8"]}
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: Tisho, Gosho")


if __name__ == '__mian__':
    main()


