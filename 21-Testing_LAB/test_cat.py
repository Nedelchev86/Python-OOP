from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Gosho")

    def test_correct_initialization(self):
        self.assertEqual(self.cat.name, "Gosho")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_cat_eat_if_fed_is_true(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_eat_if_is_hungry(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, 1)

    def test_cat_sleep_when_is_not_fed(self):
        self.cat.sleepy = True
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep_when_is_fed(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()