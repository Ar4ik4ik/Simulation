from main.entities.static import Grass
from main.entities.creature import Creature

class Herbivore(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=100, attack=1):
        super().__init__(x, y, map_instance, speed, hp, attack)

    def search_food(self):
        return self.map_instance.find_neares(self.position, Grass)


    def __repr__(self):
        return "\U0001F410"
