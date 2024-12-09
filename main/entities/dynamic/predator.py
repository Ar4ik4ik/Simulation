from main.entities.creature import Creature
from main.entities.dynamic.herbivore import Herbivore


class Predator(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=200, attack=25):
        super().__init__(x, y, map_instance, speed, hp, attack)

    def search_food(self):
        return self.map_instance.find_nearest(self.position, Herbivore)

    def attack_creature(self, creature):
        creature.health_points -= self.attack
        if not creature.check_hp():
            self.eat(creature)

    def __repr__(self):
        return "\U0001F43A"
