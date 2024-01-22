from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name):
        self.name = name
        self.quantity = self.QUANTITY
