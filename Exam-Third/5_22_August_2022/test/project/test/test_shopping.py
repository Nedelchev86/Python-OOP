from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Billa", 60.50)
        self.cart2 = ShoppingCart("Lidl", 80.50)

    def test_initialization(self):
        self.assertEqual(self.cart.shop_name, "Billa")
        self.assertEqual(self.cart.budget, 60.50)
        self.assertEqual(self.cart.products, {})

    def test_name_with_small_first_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_with_symbol_first_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "!lla"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_product_too_expensive(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 200)
        self.assertEqual(str(ve.exception), f"Product TV cost too much!")

    def test_add_product_too_expensive2(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 100)
        self.assertEqual(str(ve.exception), f"Product TV cost too much!")

    def test_add_product(self):
        result = self.cart.add_to_cart("Chocolate", 20)
        self.assertEqual(result, "Chocolate product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {"Chocolate": 20})
        self.assertEqual(self.cart.products["Chocolate"], 20)

    def test_remove_product(self):
        self.cart.add_to_cart("Chocolate", 20)
        self.cart.add_to_cart("Water", 30)
        self.assertEqual(self.cart.products, {"Chocolate": 20, "Water": 30})
        result = self.cart.remove_from_cart("Chocolate")
        self.assertEqual(result, "Product Chocolate was successfully removed from the cart!")
        self.assertEqual(self.cart.products, {"Water": 30})

    def test_remove_product_not_in_list(self):
        self.cart.add_to_cart("Chocolate", 20)
        self.cart.add_to_cart("Water", 30)
        self.assertEqual(self.cart.products, {"Chocolate": 20, "Water": 30})
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Bred")
        self.assertEqual(str(ve.exception), "No product with name Bred in the cart!")
        self.assertEqual(self.cart.products, {"Chocolate": 20, "Water": 30})


    def test_add(self):
        self.cart.add_to_cart("Chocolate", 20)
        self.cart2.add_to_cart("Water", 30)
        new_cart = self.cart + self.cart2
        self.assertEqual(new_cart.shop_name, "BillaLidl")
        self.assertEqual(new_cart.budget, 141)
        self.assertEqual(new_cart.products, {"Chocolate": 20, "Water": 30})

    def test_bue_product_With_not_enough_money(self):
        self.cart.add_to_cart("Chocolate", 20)
        self.cart.add_to_cart("Water", 60)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 19.50lv!")

    def test_bue_product_With_enough_money(self):
        self.cart.add_to_cart("Chocolate", 20)
        self.cart.add_to_cart("Water", 20)
        result = self.cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 40.00lv.')


if __name__ == '__main__':
    main()