from project.product import Product


class ProductRepository:
    # products = []

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")
        return "\n".join(result)