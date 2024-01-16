class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Gosho")

    def test_initialization(self):
        self.assertEqual(self.cat.name, "Gosho")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_eat_size_increase(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_eat_set_eat_to_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_sleepy_set_to_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_if_cat_is_fed_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_if_cat_not_eaten(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleepy_if_is_already_aet(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()