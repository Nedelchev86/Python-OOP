from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCard(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Billa", 120.50)

    def test_correct_initialization(self):
        self.assertEqual(self.cart.shop_name, "Billa")
        self.assertEqual(self.cart.budget, 120.50)
        self.assertEqual(self.cart.products, {})

    def test_name_with_first_small_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_with_first_digit(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "1illa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_product_with_expensive_protuc(self):
        self.assertEqual(self.cart.products, {})
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 200)
        self.assertEqual(str(ve.exception), "Product TV cost too much!")
        self.assertEqual(self.cart.products, {})

    def test_add_product_with_correct_price(self):
        self.assertEqual(self.cart.products, {})
        result = self.cart.add_to_cart("Meat", 20.50)
        self.assertEqual(result, "Meat product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {"Meat": 20.50})

    def test_remove_product_in_list(self):
        self.cart.add_to_cart("Meat", 20.50)
        self.cart.add_to_cart("Cheese", 10.50)
        self.assertEqual(self.cart.products, {"Meat": 20.50, "Cheese": 10.50})
        result = self.cart.remove_from_cart("Meat")
        self.assertEqual(result , "Product Meat was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {"Cheese": 10.50})

    def test_remove_product_not_in_list(self):
        self.cart.add_to_cart("Meat", 20.50)
        self.cart.add_to_cart("Cheese", 10.50)
        self.assertEqual(self.cart.products, {"Meat": 20.50, "Cheese": 10.50})
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Bred")
        self.assertEqual(str(ve.exception), "No product with name Bred in the cart!")
        self.assertEqual(self.cart.products, {"Meat": 20.50, "Cheese": 10.50})

    def test_add_method(self):
        other = ShoppingCart("Lidl", 140)
        self.cart.add_to_cart("Meat", 20.50)
        other.add_to_cart("Cheese", 10.50)
        new_shopping_cart = other + self.cart
        self.assertEqual(new_shopping_cart.shop_name, "LidlBilla")
        self.assertEqual(new_shopping_cart.budget, 260.5)
        self.assertEqual(new_shopping_cart.products, {"Meat": 20.50, "Cheese": 10.50})

    def test_buy_product_with_success(self):
        self.cart.add_to_cart("Cheese", 10.50)
        self.cart.add_to_cart("Meat", 20.50)
        result = self.cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 31.00lv.')

    def test_buy_product_with_not_enoight_budget(self):
        self.cart.add_to_cart("Cheese", 80.50)
        self.cart.add_to_cart("Meat", 40.50)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 0.50lv!")

