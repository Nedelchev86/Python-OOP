from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name):
        self.name = name
        self.quantity = self.QUANTITY
