from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTH = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(ChristmasPastryShopApp.VALID_DELICACIES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(ChristmasPastryShopApp.VALID_BOOTH[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved][0]
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        try:
            booth = [b for b in self.booths if b.booth_number == booth_number][0]
        except IndexError:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        except IndexError:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        booth.price_for_reservation = 0
        booth.is_reserved = False
        booth.delicacy_orders = []
        self.income += bill
        print(self.income)
        return f"Booth {booth.booth_number}:\nBill: {bill:.2F}lv."

    def get_income(self):
        return f"Income: {self.income:.2F}lv."

