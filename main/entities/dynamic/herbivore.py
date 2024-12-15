from main.entities.static import Grass
from main.entities.creature import Creature
from main.path_finder.path import Path


class Herbivore(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=100, attack=1):
        super().__init__(x, y, map_instance, speed, hp, attack)

    def make_move(self):
        if self._hungry < 50:
            food_obj = self.search_food()
            if food_obj:
                path = Path(self.map_instance)
                path = path.find_path(self.position, Grass)
                if path:  # Если путь найден
                    if self.position == path[-1]:
                        self.eat(food_obj)
                        return
                    else:
                        target = path[min(self.speed, len(path) - 1)]
                        self.move_towards(target)
            else:
                self.random_move()
        else:
            self.health_points += 5
            self.random_move()
        self.starve()

    def eat(self, obj):
        obj.health_points -= 1
        self.hungry += 10
        obj.check_hp()
        print(f"{self} съел траву")

    def search_food(self):
        return self.path_obj.find_nearest(self.position, Grass)

    def __repr__(self):
        return "\U0001F410"
