from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Billa", 100.50)
        self.cart2 = ShoppingCart("Lidl", 100.50)
        self.cart2.products = {"Bread": 4, "Milk": 2}

    def test_initialization(self):
        self.assertEqual("Billa", self.cart.shop_name)
        self.assertEqual(100.50, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_name_setter_with_small_first_letter_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_setter_with_first_not_letter_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "4billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_if_price_is_more_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 150)
        self.assertEqual(str(ve.exception), f"Product TV cost too much!")

    def test_add_to_Cart_with_product_less_than_100(self):
        result = self.cart.add_to_cart("Water", 5)
        self.assertEqual(self.cart.products, {"Water": 5})
        self.assertEqual(result, f"Water product was successfully added to the cart!")

    def test_remove_product_which_is_not_in_our_list(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Water")
        self.assertEqual(str(ve.exception), f"No product with name Water in the cart!")

    def test_remove_product_which_is_in_our_list(self):
        self.cart.add_to_cart("Water", 5)
        self.cart.add_to_cart("Oil", 2)
        result = self.cart.remove_from_cart("Water")
        self.assertEqual(result, "Product Water was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {"Oil": 2})

    def test_add_method(self):
        self.cart.add_to_cart("Water", 2)
        merged = self.cart + self.cart2
        self.assertEqual('BillaLidl', merged.shop_name)
        self.assertEqual(201.0, merged.budget)
        self.assertEqual({"Water": 2, "Bread": 4, "Milk": 2}, merged.products)

    def test_buy_product_with_enough_budget(self):
        self.cart.add_to_cart("Cheese", 20)
        self.cart.add_to_cart("Chocolate", 10)
        result = self.cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 30.00lv.')

    def test_buy_product_without_enough_budget(self):
        self.cart2.budget = 1
        with self.assertRaises(ValueError) as ve:
            self.cart2.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 5.00lv!")


if __name__ == '__main__':
    main()