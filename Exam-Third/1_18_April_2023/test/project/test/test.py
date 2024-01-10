from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("First", "Military", 5, 80.50)

    def test_correct_initialization(self):
        self.assertEqual(self.robot.robot_id, "First")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 5)
        self.assertEqual(self.robot.price, 80.50)

    def test_wrong_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Cooking"
        self.assertEqual(str(ve.exception), f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_negative_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -2
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_with_hardware_in_list(self):
        self.robot.hardware_upgrades = ["RAM", "CPU"]
        self.assertEqual(self.robot.hardware_upgrades, ["RAM", "CPU"])
        self.assertEqual(self.robot.price, 80.50)
        result = self.robot.upgrade("RAM", 10)
        self.assertEqual(result, "Robot First was not upgraded.")
        self.assertEqual(self.robot.price, 80.50)

    def test_upgrade_with_hardware_not_in_list(self):
        self.robot.hardware_upgrades = ["RAM"]
        self.assertEqual(self.robot.hardware_upgrades, ["RAM"])
        self.assertEqual(self.robot.price, 80.50)
        result = self.robot.upgrade("CPU", 10)
        self.assertEqual(result, 'Robot First was upgraded with CPU.')
        self.assertEqual(self.robot.price, 95.50)


    def test_ppdate_with_older_version(self):
        self.robot.software_updates = [1.2, 2.2]
        self.assertEqual(self.robot.software_updates, [1.2, 2.2])
        self.assertEqual(self.robot.available_capacity, 5)
        result = self.robot.update(2.1, 2)
        self.assertEqual(result, "Robot First was not updated.")
        self.assertEqual(self.robot.software_updates, [1.2, 2.2])
        self.assertEqual(self.robot.available_capacity, 5)

    def test_update_with_not_enough_capacity(self):
        self.robot.software_updates = [1.2, 2.2]
        self.assertEqual(self.robot.software_updates, [1.2, 2.2])
        self.assertEqual(self.robot.available_capacity, 5)
        result = self.robot.update(4.0, 8)
        self.assertEqual(result, "Robot First was not updated.")
        self.assertEqual(self.robot.software_updates, [1.2, 2.2])
        self.assertEqual(self.robot.available_capacity, 5)

    def test_successful_update(self):
        self.robot.software_updates = [1.2, 2.2]
        self.assertEqual(self.robot.software_updates, [1.2, 2.2])
        self.assertEqual(self.robot.available_capacity, 5)
        result = self.robot.update(4.5, 4)
        self.assertEqual(result, 'Robot First was updated to version 4.5.')
        self.assertEqual(self.robot.software_updates, [1.2, 2.2, 4.5])
        self.assertEqual(self.robot.available_capacity, 1)

    def test_gt_method_first_more_expensive(self):
        robot2 = Robot("Second", "Education", 6, 70.50)
        result = self.robot > robot2
        self.assertEqual(result, 'Robot with ID First is more expensive than Robot with ID Second.')

    def test_gt_method_first_eq_Second(self):
        robot2 = Robot("Second", "Education", 6, 80.50)
        result = self.robot > robot2
        self.assertEqual(result, 'Robot with ID First costs equal to Robot with ID Second.')

    def test_gt_method_first_cheaper(self):
        robot2 = Robot("Second", "Education", 6, 90.50)
        result = self.robot > robot2
        self.assertEqual(result, 'Robot with ID First is cheaper than Robot with ID Second.')

if __name__ == '__main__':
    main()