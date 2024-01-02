from unittest import TestCase, main

class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase, main

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 2000, 50)

    def test_worker_correct_initialization(self):
        self.assertEqual(self.worker.name, 'Ivan')
        self.assertEqual(self.worker.salary, 2000)
        self.assertEqual(self.worker.energy, 50)
        self.assertEqual(self.worker.money, 0)

    def test_worker_work_with_energy_more_than_zero(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 2000)
        self.assertEqual(self.worker.energy, 49)

    def test_worker_work_without_enough_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_function(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 51)

    def test_get_info(self):
        expected_result = self.worker.get_info()
        self.assertEqual(f'Ivan has saved 0 money.', expected_result)


if __name__ == '__main__':
    main()
