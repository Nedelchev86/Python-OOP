from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Tihomir", 2.0)

    def test_correct_initialization(self):
        self.assertEqual(self.driver.name, "Tihomir")
        self.assertEqual(self.driver.money_per_mile, 2.0)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_monet_with_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -5
        self.assertEqual(str(ve.exception), "Tihomir went bankrupt.")

    def test_earned_monet_with_positive_number(self):
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.earned_money = 100
        self.assertEqual(self.driver.earned_money, 100)

    def test_add_cargo_offer_is_already_Added(self):
        self.driver.available_cargos = {"Bourgas": 100, "Varna": 150}
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 100, "Varna": 150})
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Bourgas", 50)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 100, "Varna": 150})

    def test_add_cargo_offer_not_added(self):
        self.driver.available_cargos = {"Bourgas": 100}
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 100})
        result = self.driver.add_cargo_offer("Sofia", 50)
        self.assertEqual(result, "Cargo for 50 to Sofia was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 100, "Sofia": 50})

    def test_drive_best_cargo_with_no_available_cargos(self):
        self.assertEqual(self.driver.available_cargos, {})
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_driver_went_bankrut(self):
        self.driver.money_per_mile = 0.1
        self.driver.earned_money = 10
        self.driver.available_cargos = {"Sofia": 5000}
        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(ve.exception), "Tihomir went bankrupt.")

    def test_drive_best_cargo_with_real_cargos(self):
        self.driver.add_cargo_offer("Bourgas", 50)
        self.driver.add_cargo_offer("Sofia", 100)
        self.driver.add_cargo_offer("Varna", 120)
        self.assertEqual(self.driver.available_cargos, {"Bourgas": 50, "Sofia": 100, "Varna": 120})
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 240.0)
        self.assertEqual(self.driver.miles, 120)
        self.assertEqual(result, "Tihomir is driving 120 to Varna.")

    def test_try_best_cargo_with_available_cargos_with_10000_miles(self):
        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Bourgas": 100, "Varna": 10000}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "Tihomir is driving 10000 to Varna.")
        self.assertEqual(self.driver.miles, 10000)
        self.assertEqual(self.driver.earned_money, 38250)

    def test_check_for_activities(self):
        self.driver.miles = 10000
        self.driver.earned_money = 100000
        self.driver.check_for_activities(1000)
        self.assertEqual(self.driver.miles, 10000)
        self.assertEqual(self.driver.earned_money, 99875)

    def test_repr(self):
        self.driver.miles = 100
        self.assertEqual(repr(self.driver), "Tihomir has 100 miles behind his back.")



if __name__ == '__main__':
    main()