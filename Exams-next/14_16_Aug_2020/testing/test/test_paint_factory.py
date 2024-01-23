from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestFactory(TestCase):

    def setUp(self) -> None:
        self.paint = PaintFactory("Tihomir", 5)

    def test_initialization(self):
        self.assertEqual(self.paint.name, "Tihomir")
        self.assertEqual(self.paint.capacity, 5)
        self.assertEqual(self.paint.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint.ingredients, {})
        self.assertEqual({}, self.paint.products)

    def test_add_ingredients_if_product_Type_in_list(self):
        self.paint.add_ingredient("white", 3)
        self.assertEqual(self.paint.ingredients["white"], 3)
        self.assertEqual(self.paint.ingredients, {"white": 3})
        with self.assertRaises(ValueError) as ve:
            self.paint.add_ingredient("white", 3)
        self.assertEqual(str(ve.exception), "Not enough space in factory")
        self.assertEqual(self.paint.ingredients["white"], 3)
        self.assertEqual(self.paint.ingredients, {"white": 3})

        with self.assertRaises(TypeError) as te:
            self.paint.add_ingredient("trash", 1)
        self.assertEqual(str(te.exception), "Ingredient of type trash not allowed in PaintFactory")

    def test_remove_ingredient(self):
        self.paint.add_ingredient("white", 3)
        self.paint.add_ingredient("blue", 2)
        self.paint.remove_ingredient("white", 1)
        self.assertEqual(self.paint.ingredients["white"], 2)
        with self.assertRaises(ValueError) as ve:
            self.paint.remove_ingredient("white", 4)
        self.assertEqual(str(ve.exception), "Ingredients quantity cannot be less than zero")
        self.assertEqual(self.paint.ingredients["white"], 2)

        with self.assertRaises(KeyError) as ke:
            self.paint.remove_ingredient("trash", 4)
        self.assertEqual(str(ke.exception), "'No such ingredient in the factory'")


if __name__ == '__main__':
    main()