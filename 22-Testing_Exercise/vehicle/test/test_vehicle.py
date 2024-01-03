from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20, 170)

    def test_correct_initialization(self):
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.fuel, 20)
        self.assertEqual(self.vehicle.horse_power, 170)
        self.assertEqual(self.vehicle.capacity, 20)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_refuel_with_more_fuel_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_amount(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(5)
        self.assertEqual(15, self.vehicle.fuel)

    def test_str_method(self):
        self.assertEqual("The vehicle has 170 horse power"
                         " with 20 fuel left and 1.25 fuel consumption",
                         str(self.vehicle))


if __name__ == '__main__':
    main()