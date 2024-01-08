from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = [m.details() for m in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.register_client(client_phone_number)

        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        for name, quantity in meal_names_and_quantities.items():
            if name not in [m.name for m in self.menu]:
                raise Exception(f"{name} is not on the menu!")
            meal = [m for m in self.menu if name == m.name][0]
            if quantity > meal.quantity:
                raise Exception(F"Not enough quantity of {meal.__class__.__name__}: {name}!")

        for name, quantity in meal_names_and_quantities.items():
            meal = [m for m in self.menu if name == m.name][0]
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

            if meal not in client.ordered:
                client.ordered[meal.name] = 0
            client.ordered[meal.name] += quantity

        return f"Client {client.phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2F}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.ordered.items():
            meal = [m for m in self.menu if meal_name == m.name][0]
            meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.ordered = {}

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = [c for c in self.clients_list if client_phone_number == c.phone_number][0]
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        FoodOrdersApp.receipt_id += 1
        current_bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        client.ordered = {}
        return f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {current_bill:.2F} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
