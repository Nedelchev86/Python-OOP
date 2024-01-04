from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("2", "Military", 3, 100)

    def test_initialization(self):
        self.assertEqual("2", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(3, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Programmer"
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_setter_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_if_component_already_added(self):
        self.robot.hardware_upgrades = ["RAM", "MEMORY"]
        result = self.robot.upgrade("RAM", 20)
        self.assertEqual("Robot 2 was not upgraded.", result)

    def test_upgrade_with_new_component(self):
        self.robot.hardware_upgrades = ["RAM", "MEMORY"]
        result = self.robot.upgrade("Test", 20)
        self.assertEqual(f'Robot 2 was upgraded with Test.', result)
        self.assertEqual(self.robot.price, 130)
        self.assertEqual(self.robot.hardware_upgrades, ["RAM", "MEMORY", "Test"])

    def test_update_with_older_version(self):
        self.robot.software_updates = [2]
        result = self.robot.update(1, 2)
        self.assertEqual("Robot 2 was not updated.", result)

    def test_update_with_new_version_but_not_enough_capacity(self):
        self.robot.software_updates = [2]
        result = self.robot.update(3, 4)
        self.assertEqual("Robot 2 was not updated.", result)

    def test_update_successful(self):
        self.robot.software_updates = [2]
        result = self.robot.update(3, 2)
        self.assertEqual(self.robot.software_updates, [2, 3])
        self.assertEqual(self.robot.available_capacity, 1)
        self.assertEqual(result, 'Robot 2 was updated to version 3.')

    def test_gt_method_with_first_gr(self):
        self.robot2 = Robot("3", "Education", 2, 50)
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 2 is more expensive than Robot with ID 3.', result)

    def test_gt_method_with_first_ew_second(self):
        self.robot2 = Robot("3", "Education", 2, 100)
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 2 costs equal to Robot with ID 3.', result)

    def test_gt_method_with_first_low_second(self):
        self.robot2 = Robot("3", "Education", 2, 110)
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 2 is cheaper than Robot with ID 3.', result)


if __name__ == '__main__':
    main()