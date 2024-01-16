from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Tihomir", 10, 100.50, 50.50)
        self.enemy = Hero("Enemy", 10, 50.50, 20.50)

    def test_initialization(self):
        self.assertEqual(self.hero.username, "Tihomir")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100.50)
        self.assertEqual(self.hero.damage, 50.50)

    def test_battle_method_with_enemy_with_same_name(self):
        self.enemy.username = "Tihomir"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_without_enough_hero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_without_enough_enemy_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_with_enough_enemy_and_hero_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, -104.50)
        self.assertEqual(self.enemy.health, -454.50)

    def test_battle_with_enemy_if_both_health_is_0(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_with_hero_more_health_after_battle(self):
        self.hero.health = 10000
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 9800)
        self.assertEqual(self.hero.damage, 55.50)

    def test_battle_with_hero_less_health_after_battle(self):
        self.enemy.health = 1000
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(self.enemy.level, 11)
        self.assertEqual(self.enemy.health, 500)
        self.assertEqual(self.enemy.damage, 25.50)

    def test_str(self):
        expected_result = f"Hero Tihomir: 10 lvl\n" \
               f"Health: 100.5\n" \
               f"Damage: 50.5\n"
        result = str(self.hero)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()