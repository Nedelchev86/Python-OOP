from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 1000, 10)

    def test_initialization(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_enough_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)
        self.assertEqual(self.worker.money, 1000)

    def test_rest_is_energy_correct(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_is_info_correct(self):
        self.assertEqual(self.worker.get_info(), "Ivan has saved 0 money.")


if __name__ == '__main__':
    main()