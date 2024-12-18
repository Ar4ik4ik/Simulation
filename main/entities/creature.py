from abc import abstractmethod
from main.entities.entity import Entity
from main.path_finder.path import Path
import random


class Creature(Entity):
    def __init__(self, x, y, map_instance, speed, hp, attack):
        super().__init__(x, y, map_instance)
        self._health_points = hp
        self.attack = attack
        self._hungry = 100
        self.speed = speed
        self.max_health_points = hp
        self.path_obj = Path(map_instance)

    # Метод, который будет вызываться каждый ход, для отслеживания состояний сущностей
    def check_hp(self):
        if self.health_points <= 0:
            self.map_instance.delete_from_cell(*self.position)

    # Метод, который используется в проверке, если не ест, то голодает и идет к еде
    def starve(self):
        if self._hungry <= 0:
            self._hungry = 0
            self.health_points -= 2
        else:
            self._hungry -= 2

    @abstractmethod
    def interact_with_food(self, food):
        pass

    def make_move(self):
        if self._hungry < 50:
            food_obj, food_dist = self.search_food().values()

            if food_dist == 1:
                self.interact_with_food(food_obj)
            elif food_obj:  # Тут проверяется что объект != None

                path = Path(self.map_instance)
                path = path.find_path(self.position, food_obj)
                if path:  # Если путь найден
                    if self.position == path[-1]:
                        self.interact_with_food(food_obj)
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

    def random_move(self):
        x, y = self.position
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(directions)
        for nx, ny in directions:
            if self.map_instance.complex_check(nx, ny):
                self.move_towards((nx, ny))
                break

    def move_towards(self, target):
        if self.map_instance.check_cell(*target) or self.map_instance.is_grass(*target):
            old_position = self.position
            self.position = target
            self.map_instance.move_entity(old_position, target)

    @abstractmethod
    def eat(self, obj):
        pass

    @abstractmethod
    def search_food(self):
        pass

    @property
    @abstractmethod
    def food_type(self):
        pass

    @property
    def hungry(self):
        return self._hungry

    @hungry.setter
    def hungry(self, value):
        if value >= 100:
            self._hungry = 100

        elif value <= 0:
            self._hungry = 0

        else:
            self._hungry = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value > self.max_health_points:
            self._health_points = self.max_health_points

        elif value <= 0:
            self._health_points = 0

        else:
            self._health_points = value

        self.check_hp()

    def __repr__(self):
        return 'C'
