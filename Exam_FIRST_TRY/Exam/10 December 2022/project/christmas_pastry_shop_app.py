from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    delicacy_name = []
    type_of_delicacy = ["Gingerbread", "Stolen"]
    booths_numbers = []
    booths_type = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in self.delicacy_name:
            raise Exception(f"{name} already exists!")
        self.delicacy_name.append(name)
        if type_delicacy not in self.type_of_delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in self.booths_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")
        self.booths_numbers.append(booth_number)
        if type_booth not in self.booths_type:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.is_reserved = True
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                for delicacie in self.delicacies:
                    if delicacie.name == delicacy_name:
                        booth.delicacy_orders.append(delicacie.price)
                        return f"Booth {booth_number} ordered {delicacy_name}."
                raise Exception(f"No {delicacy_name} in the pastry shop!")
        raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                bill = sum(booth.delicacy_orders) + booth.price_for_reservation
                booth.price_for_reservation = 0
                booth.delicacy_orders = []
                booth.is_reserved = False
                self.income += bill
                return f"Booth {booth_number}:\nBill: {bill:.2F}lv."

    def get_income(self):
        return f"Income: {self.income:.2F}lv."
    