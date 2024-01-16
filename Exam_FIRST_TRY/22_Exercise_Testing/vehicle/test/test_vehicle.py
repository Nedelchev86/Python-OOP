from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 170)

    def test_initialization(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.horse_power, 170)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_method_if_dont_have_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_if_have_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.50)

    def test_refuel_method_if_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_if_fuel_is_less_than_capacity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 10)

    def test_str_method(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 170 " \
               f"horse power with 50 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    main()