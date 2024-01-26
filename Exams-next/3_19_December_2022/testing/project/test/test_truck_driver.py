from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Tihomir", 1.0)

    def test_correct_initialization(self):
        self.assertEqual(self.driver.name, "Tihomir")
        self.assertEqual(self.driver.money_per_mile, 1.0)
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)
        self.assertEqual(self.driver.available_cargos, {})

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(str(ve.exception), "Tihomir went bankrupt.")

    def test_earned_money_with_possitive_amount(self):
        self.driver.earned_money = 10
        self.assertEqual(self.driver.earned_money, 10)

    def test_add_cargo_with_cargo_already_in_dict(self):
        self.driver.available_cargos["Bourgas"] = 100
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Bourgas", 100)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo(self):
        result = self.driver.add_cargo_offer("Bourgas", 100)
        self.assertEqual(result, "Cargo for 100 to Bourgas was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 100})
        self.assertEqual(self.driver.available_cargos["Bourgas"], 100)

    def test_try_best_cargo_with_empy_cargo_dict(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_try_best_cargo_with_available_cargos(self):
        self.driver.available_cargos = {"Bourgas": 100, "Varna": 200}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Tihomir is driving 200 to Varna.")
        self.assertEqual(self.driver.earned_money, 200.0)
        self.assertEqual(self.driver.miles, 200)

    def test_try_best_cargo_with_available_cargos_with_500_miles(self):
        self.driver.available_cargos = {"Bourgas": 100, "Varna": 1000}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Tihomir is driving 1000 to Varna.")
        self.assertEqual(self.driver.miles, 1000)
        self.assertEqual(self.driver.earned_money, 875.0)

    def test_try_best_cargo_with_available_cargos_with_10000_miles(self):
        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Bourgas": 100, "Varna": 10000}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Tihomir is driving 10000 to Varna.")
        self.assertEqual(self.driver.miles, 10000)
        self.assertEqual(self.driver.earned_money, 38250)

    def test_repr(self):
        self.driver.miles = 100
        self.assertEqual("Tihomir has 100 miles behind his back.", str(self.driver))


if __name__ == '__main__':
    main()