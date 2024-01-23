from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet = PetShop("Tihomir")

    def test_initialization(self):
        self.assertEqual(self.pet.name, "Tihomir")
        self.assertEqual(self.pet.food, {})
        self.assertEqual(self.pet.pets, [])

    def test_add_food_with_zero_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet.add_food("Tihomir", 0)
        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_with_negative_quantity(self):
        with self.assertRaises(ValueError) as ve:
            self.pet.add_food("Tihomir", -1)
        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_with_correct_quantity_but_name_not_in_dict(self):
        result = self.pet.add_food("Gosho", 2.5)
        self.assertEqual(result, "Successfully added 2.50 grams of Gosho.")
        self.assertEqual(self.pet.food, {"Gosho": 2.5})
        self.assertEqual(self.pet.food["Gosho"], 2.5)

    def test_add_food_with_correct_quantity_but_name_in_dict(self):
        self.pet.add_food("Gosho", 2.0)
        result = self.pet.add_food("Gosho", 2.5)
        self.assertEqual(result, "Successfully added 2.50 grams of Gosho.")
        self.assertEqual(self.pet.food, {"Gosho": 4.5})
        self.assertEqual(self.pet.food["Gosho"], 4.5)

    def test_add_pet_with_name_not_in_list(self):
        self.pet.pets = ["Pesho"]
        result = self.pet.add_pet("Gosho")
        self.assertEqual(result, f"Successfully added Gosho.")
        self.assertEqual(self.pet.pets, ["Pesho", "Gosho"])

    def test_add_pet_with_name_already_in_list(self):
        self.pet.pets = ["Gosho"]
        with self.assertRaises(Exception) as ex:
            self.pet.add_pet("Gosho")
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")
        self.assertEqual(self.pet.pets, ["Gosho"])

    def test_feed_pet_with_name_not_in_pets(self):
        with self.assertRaises(Exception) as ex:
            self.pet.feed_pet("Gosho", "Pesho")
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_with_food_name_not_in_pets(self):
        self.pet.add_food("Test", 2.5)
        self.pet.pets = ["Pesho"]
        result = self.pet.feed_pet("Gosho", "Pesho")
        self.assertEqual(result, 'You do not have Gosho')

    def test_feed_pets_with_correct_input_but_food_less_than_100(self):
        self.pet.add_pet("Gosho")
        self.pet.add_food("grass", 60.0)
        result = self.pet.feed_pet("grass", "Gosho")
        self.assertEqual(self.pet.food["grass"], 1060.00)
        self.assertEqual(result, "Adding food...")

    def test_feed_pets_with_correct_input_but_food_more_than_100(self):
        self.pet.add_pet("Gosho")
        self.pet.add_food("grass", 150.0)
        result = self.pet.feed_pet("grass", "Gosho")
        self.assertEqual(self.pet.food["grass"], 50.00)
        self.assertEqual(result, "Gosho was successfully fed")

    def test_repr_methods(self):
        self.pet.add_pet("Gosho")
        self.pet.add_pet("Pesho")
        result = "Shop Tihomir:\nPets: Gosho, Pesho"
        self.assertEqual(result, repr(self.pet))

if __name__ == '__main__':
    main()