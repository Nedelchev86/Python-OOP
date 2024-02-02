from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Billa", 100.50)
        self.cart2 = ShoppingCart("Lidl", 50.50)

    def test_correct_initialization(self):
        self.assertEqual(self.cart.shop_name, "Billa")
        self.assertEqual(self.cart.budget, 100.50)
        self.assertEqual(self.cart.products, {})

    def test_set_shop_name_is_with_first_small_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_set_shop_name_is_with_number(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "bil2la"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_product_with_price_more_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("PC", 1000)
        self.assertEqual(str(ve.exception), "Product PC cost too much!")

    def test_add_product_with_price_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("PC", 100)
        self.assertEqual(str(ve.exception), "Product PC cost too much!")

    def test_add_to_Cart_with_correct_price(self):
        result = self.cart.add_to_cart("IQOS", 70)
        self.assertEqual(result, "IQOS product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {"IQOS": 70})
        self.assertEqual(self.cart.products["IQOS"], 70)

    def test_remove_product_if_product_not_in_dict(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("IQOS")
        self.assertEqual(str(ve.exception), "No product with name IQOS in the cart!")

    def test_remove_product_if_product_in_dict(self):
        self.cart.products = {"IQOS": 70, "Test": 50}
        result = self.cart.remove_from_cart("Test")
        self.assertEqual(result, "Product Test was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {"IQOS": 70})

    def test_add_method(self):
        self.cart.products = {"IQOS": 20}
        self.cart2.products = {"Test": 100}
        new_shop = self.cart + self.cart2
        self.assertEqual(new_shop.shop_name, "BillaLidl")
        self.assertEqual(new_shop.budget, 151)
        self.assertEqual(new_shop.products, {"IQOS": 20, "Test": 100})

    def test_buy_product_with_not_enough_budget(self):
        self.cart.products = {"Test": 60, "Test2": 90, "Test3": 70}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 119.50lv!")

    def test_buy_product_with_enough_budget(self):
        self.cart.products = {"Test": 60, "Test2": 30}
        result = self.cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 90.00lv.')

if __name__ == '__main__':
    main()