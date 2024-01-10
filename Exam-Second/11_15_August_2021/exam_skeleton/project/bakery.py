from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    FOOD_TYPE = {
        "Bread": Bread,
        "Cake": Cake,
    }

    DRINK_TYPE = {
        "Tea": Tea,
        "Water": Water,
    }

    TABLE_TYPE = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in Bakery.FOOD_TYPE:
            return

        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(Bakery.FOOD_TYPE[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in Bakery.DRINK_TYPE:
            self.drinks_menu.append(Bakery.DRINK_TYPE[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(Bakery.TABLE_TYPE[table_type](table_number, capacity))

    def reserve_table(self, number_of_people: int):
        try:
            table = [t for t in self.tables_repository if t.capacity >= number_of_people and not t.is_reserved][0]
        except IndexError:
            return f"No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_name):
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        in_menu = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.__class__.__name__} does not have in the menu:"]

        for food in food_name:
            if food in [f.name for f in self.food_menu]:
                current_menu = [f for f in self.food_menu if food == f.name][0]
                table.order_food(current_menu)
                in_menu.append(repr(current_menu))
            else:
                not_in_menu.append(food)
        in_menu.extend(not_in_menu)
        return "\n".join(in_menu)


    def order_drink(self, table_number: int, *drinks_name):
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        in_menu = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.__class__.__name__} does not have in the menu:"]

        for drink in drinks_name:
            if drink in [d.name for d in self.drinks_menu]:
                current_menu = [d for d in self.drinks_menu if drink == d.name][0]
                table.order_drink(current_menu)
                in_menu.append(repr(current_menu))
            else:
                not_in_menu.append(drink)
        in_menu.extend(not_in_menu)
        return "\n".join(in_menu)

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2F}"

    def get_free_tables_info(self):
        result = []
        for t in self.tables_repository:
            result.append(t.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2F}lv"
