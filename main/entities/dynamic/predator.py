from main.entities.dynamic.creature import Creature
from main.entities.dynamic.herbivore import Herbivore


class Predator(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=200, attack=25):
        super().__init__(x, y, map_instance, speed, hp, attack)
        self._food_type = Herbivore

    def eat(self, obj):
        self.hungry += 20
        obj.check_hp()
        print(f"{self.__class__.__name__} съел {obj.__class__.__name__}")

    def search_food(self) -> dict[str, type[Herbivore] | int]:
        return self.path_obj.find_nearest(self.position, Herbivore)

    def interact_with_food(self, creature):
        creature.health_points -= self.attack
        print(f"Predator атаковал Herbivore")
        if creature.health_points <= 0:
            self.eat(creature)
            print(f"Predator съел Herbivore")

    def __repr__(self):
        return "\U0001F43A"

    @property
    def food_type(self):
        return self._food_type
