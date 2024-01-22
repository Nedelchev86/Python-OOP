from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Tihomir", 2)

    def test_initialization(self):
        self.assertEqual("Tihomir", self.driver.name)
        self.assertEqual(2, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_with_negative_amount(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -5
        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_earned_money_setter_with_positive_amount(self):
        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)

    def test_add_cargo_offer_if_already_in_available_cargos(self):
        self.driver.available_cargos = {"Bourgas": 5}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Bourgas", 5)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_if_not_in_available_cargos(self):
        self.driver.add_cargo_offer("Bourgas", 5)
        self.assertEqual({"Bourgas": 5}, self.driver.available_cargos)

    def test_add_cargo_offer_if_not_in_available_cargos_test_return(self):
        result = self.driver.add_cargo_offer("Bourgas", 5)
        self.assertEqual("Cargo for 5 to Bourgas was added as an offer.", result)

    def test_drive_best_cargo_offer_with_no_offers_available(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_with_valid_offers_available(self):
        self.driver.add_cargo_offer("Bourgas", 5)
        self.driver.add_cargo_offer("Varna", 20000)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(16000, self.driver.earned_money)
        self.assertEqual(20000, self.driver.miles)
        self.assertEqual(f"{self.driver.name} is driving 20000 to Varna.", result)


    def test_eat_with_250(self):
        self.driver.earned_money = 41
        self.driver.eat(500)
        self.driver.eat(1000)
        self.assertEqual(1, self.driver.earned_money)

    def test_sleep_with_1000(self):
        self.driver.earned_money = 91
        self.driver.sleep(1000)
        self.driver.sleep(2000)
        self.assertEqual(1, self.driver.earned_money)

    def test_pump_gas_with_1500(self):
        self.driver.earned_money = 1001
        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)
        self.assertEqual(1, self.driver.earned_money)

    def test_repair_truck_with_1500(self):
        self.driver.earned_money = 15001
        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)
        self.assertEqual(1, self.driver.earned_money)

    def test_repr(self):
        result = str(self.driver)
        self.assertEqual("Tihomir has 0 miles behind his back.", result)














if __name__ == '__main__':
    main()

