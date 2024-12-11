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
            self.check_hp()
        else:
            self._hungry -= 2

    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def eat(self, obj):
        pass

    @abstractmethod
    def search_food(self):
        pass

    def random_move(self):
        x, y = self.position
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(directions)

        for nx, ny in directions:
            if self.map_instance.check_bounds(nx, ny) and self.map_instance.check_cell(nx, ny):
                self.move_towards((nx, ny))
                break

    def move_towards(self, target):
        if self.map_instance.check_cell(*target):
            old_position = self.position
            self.position = target
            self.map_instance.move_entity(old_position, target)

    @property
    def hungry(self):
        return self._hungry

    @hungry.setter
    def hungry(self, value):
        if self._hungry + value >= 100:
            self._hungry = 100
            return
        self._hungry += value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if self._health_points + value > self.max_health_points:
            self._health_points = self.max_health_points
            return
        self._health_points += value
        self.check_hp()

    def __repr__(self):
        return 'C'
