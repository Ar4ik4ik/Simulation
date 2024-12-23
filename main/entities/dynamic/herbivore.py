from main.entities.static import Grass
from main.entities.dynamic.creature import Creature


class Herbivore(Creature):
    def __init__(self, x, y, map_instance, speed=3, hp=100, attack=1):
        super().__init__(x, y, map_instance, speed, hp, attack)
        self._food_type = Grass

    def interact_with_food(self, food: Grass):
        self.eat(food)

    def eat(self, food: Grass):
        food.health_points -= self.attack
        self.hungry += 20
        food.check_hp()
        print(f"{self} съел траву")

    def search_food(self) -> dict[str, type[Grass] | int]:
        nearest_food = self.path_obj.find_nearest(self.position, Grass)
        return nearest_food

    def __repr__(self):
        return "\U0001F410"

    @property
    def food_type(self):
        return self._food_type
