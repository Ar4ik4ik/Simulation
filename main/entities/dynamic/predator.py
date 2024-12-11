from main.entities.creature import Creature
from main.entities.dynamic.herbivore import Herbivore
from main.path_finder.path import Path
class Predator(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=200, attack=25):
        super().__init__(x, y, map_instance, speed, hp, attack)

    def make_move(self):
        if self._hungry < 50:
            food_obj = self.search_food() or None
            if food_obj:
                path = Path(self.map_instance)
                path = path.find_path(self.position, Herbivore)
                if path:  # Если путь найден
                    if self.position == path[-1]:
                        self.attack(food_obj)
                    else:
                        self.starve()
                        target = path[min(self.speed, len(path) - 1)]
                        self.move_towards(target)
            else:
                self.random_move()
        else:
            self.health_points += 5
            self.random_move()

    def eat(self, obj):
        self._hungry += 20
        obj.check_hp()
        print(f"{self.__class__.__name__} съел {obj.__class__.__name__}")

    def search_food(self):
        return self.path_obj.find_nearest(self.position, Herbivore)

    def attack_creature(self, creature):
        creature.health_points -= self.attack
        if creature.health_points <= 0:
            self.eat(creature)

    def __repr__(self):
        return "\U0001F43A"
