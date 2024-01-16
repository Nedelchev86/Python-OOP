from unittest import TestCase, main
from car_manager import Car


class CarTest(TestCase):

    def setUp(self):
        self.opel = Car("Opel", "Insignia", 6, 50)

    def test_initialization(self):
        self.assertEqual(self.opel.make, "Opel")
        self.assertEqual(self.opel.model, "Insignia")
        self.assertEqual(self.opel.fuel_consumption, 6)
        self.assertEqual(self.opel.fuel_capacity, 50)
        self.assertEqual(self.opel.fuel_amount, 0)

    def test_make_car_with_empty_name(self):
        with self.assertRaises(Exception) as ex:
            self.opel.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_car_model_with_empty_name(self):
        with self.assertRaises(Exception) as ex:
            self.opel.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_make_car_with_wrong_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.opel.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_make_car_with_wrong_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.opel.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_make_car_with_wrong_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.opel.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_with_zero_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.opel.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!",str(ex.exception))

    def test_refuel_method_with_positive_fuel(self):
        self.opel.refuel(100)
        self.assertEqual(self.opel.fuel_amount, self.opel.fuel_capacity)

    def test_drive_method_with_enough_fuel(self):
        self.opel.fuel_amount = self.opel.fuel_capacity
        self.opel.drive(100)
        self.assertEqual(self.opel.fuel_amount, 44)

    def test_drive_method_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.opel.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()