from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1", "Military", 5, 100.50)
        self.robot2 = Robot("2", "Education", 4, 50.50)

    def test_initialization_with_correct_data(self):
        self.assertEqual(self.robot.robot_id, "1")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 5)
        self.assertEqual(self.robot.price, 100.5)
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])

    def test_wrong_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Test"
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_with_negative_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -5
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_with_existing_upgrade(self):
        self.robot.hardware_upgrades.append("weapon")
        result = self.robot.upgrade("weapon", 100)
        self.assertEqual(result, "Robot 1 was not upgraded.")

    def test_upgrade_with_Correct_input(self):
        result = self.robot.upgrade("weapon", 100)
        self.assertEqual(result, 'Robot 1 was upgraded with weapon.')
        self.assertEqual(self.robot.hardware_upgrades, ["weapon"])
        self.assertEqual(self.robot.price, 250.5)

    def test_update_with_older_version(self):
        self.robot.software_updates.append(1.1)
        self.robot.software_updates.append(1.2)
        result = self.robot.update(1, 2)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_update_with_not_enough_capacity(self):
        self.robot.software_updates.append(1.1)
        self.robot.software_updates.append(1.2)
        result = self.robot.update(2, 6)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_update_with_correct_data(self):
        self.robot.software_updates.append(1.1)
        self.robot.software_updates.append(1.2)
        result = self.robot.update(2.1, 4)
        self.assertEqual(self.robot.available_capacity, 1)
        self.assertEqual("Robot 1 was updated to version 2.1.", result)
        self.assertEqual(self.robot.software_updates, [1.1, 1.2, 2.1])

    def test_gt_method_with_price_of_first_greater_than_second(self):
        result = self.robot > self.robot2
        self.assertEqual(f'Robot with ID 1 is more expensive than Robot with ID 2.', result)

    def test_gt_method_with_same_price(self):
        self.robot2.price = 100.5
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 1 costs equal to Robot with ID 2.', result)

    def test_gt_method_with_price_of_first_lower_than_second(self):
        self.robot.price = 50.20
        result = self.robot > self.robot2
        self.assertEqual('Robot with ID 1 is cheaper than Robot with ID 2.', result)


if __name__ == "__main__":
    main()