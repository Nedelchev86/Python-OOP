from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Gosho", "cat", "miau")

    def test_initialization(self):
        self.assertEqual(self.mammal.name, "Gosho")
        self.assertEqual(self.mammal.type, "cat")
        self.assertEqual(self.mammal.sound, "miau")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Gosho makes miau")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_get_info(self):
        self.assertEqual(self.mammal.info(), "Gosho is of type cat")



if __name__ == '__main__':
    main()