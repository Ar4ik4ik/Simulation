from main.entities.creature import Creature
from main.entities.dynamic.herbivore import Herbivore
from main.path_finder.path import Path


class Predator(Creature):
    def __init__(self, x, y, map_instance, speed=2, hp=200, attack=25):
        super().__init__(x, y, map_instance, speed, hp, attack)

    def make_move(self):
        if self._hungry < 50:
            food_obj = self.search_food()

            if food_obj[1] == 1:
                self.attack_creature(food_obj[0])

            elif food_obj[0]:
                path = Path(self.map_instance)
                path = path.find_path(self.position, Herbivore)
                if path:  # Если путь найден
                    if self.position == path[-1]:
                        self.attack_creature(food_obj)
                        return
                    else:
                        target = path[min(self.speed, len(path) - 1)]
                        self.move_towards(target)
            else:
                print(f"Еда для {self.__class__.__name__} не найдена")
                self.random_move()
        else:
            self.health_points += 5
            self.random_move()
        self.starve()

    def eat(self, obj):
        self.hungry += 20
        obj.check_hp()
        print(f"{self.__class__.__name__} съел {obj.__class__.__name__}")

    def search_food(self):
        return self.path_obj.find_nearest(self.position, Herbivore)

    def attack_creature(self, creature):
        creature.health_points -= self.attack
        print(f"Predator атаковал Herbivore")
        if creature.health_points <= 0:
            self.eat(creature)
            print(f"Predator съел Herbivore")

    def __repr__(self):
        return "\U0001F43A"
