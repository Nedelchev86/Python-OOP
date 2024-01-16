class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def defend(self, damage,):
        if damage >= self.health:
            self.health = 0
            return F"{self.name} was defeated"

        self.health -= damage

    def heal(self, amount):
        self.health += amount











hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))