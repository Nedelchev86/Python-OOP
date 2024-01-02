from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("Tihomir", 10, 100, 50)
        self.enemy_hero = Hero("Gosho", 5, 90, 40)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "Tihomir")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

        self.assertEqual(self.enemy_hero.username, "Gosho")
        self.assertEqual(self.enemy_hero.level, 5)
        self.assertEqual(self.enemy_hero.health, 90)
        self.assertEqual(self.enemy_hero.damage, 40)

    def test_battle_with_same_hero(self):
        with self.assertRaises(Exception) as ex:
            self.enemy_hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with__enemy_with_zero_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_battle_with_two_heroes_with_zero_health_after_battle(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_enemy_health_zero_after_battle(self):
        self.enemy_hero.level = 1
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 65)
        self.assertEqual(self.hero.damage, 55)

    def test_my_hero_health_zero_after_battle(self):
        self.hero.level = 1
        self.hero.health = 10
        self.hero.damage = 10
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(self.enemy_hero.level, 6)
        self.assertEqual(self.enemy_hero.health, 85)
        self.assertEqual(self.enemy_hero.damage, 45)

    def test_str_method(self):
        self.assertEqual(
            f"Hero Tihomir: 10 lvl\n" \
            f"Health: 100\n" \
            f"Damage: 50\n",
            str(self.hero)
        )

if __name__ == '__main__':
    main()