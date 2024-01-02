from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Pesho", "dog", "bau")

    def test_correct_initialization(self):
        self.assertEqual(self.mammal.name, "Pesho")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bau")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_Sound(self):
        self.assertEqual(self.mammal.make_sound(), "Pesho makes bau")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Pesho is of type dog")


if __name__ == '__main__':
    main()