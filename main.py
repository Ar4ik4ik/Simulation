from abc import ABC, abstractmethod
import random
from random import choice


class Entity(ABC):
    def __init__(self, x, y):
        self.position = (x, y)

    @abstractmethod
    def __str__(self):
        pass


class Grass(Entity):
    def __str__(self):
        return 'G'


class Rock(Entity):
    def __str__(self):
        return 'R'


class Tree(Entity):
    def __str__(self):
        return 'T'


class Creature(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._health_points = 100
        self._hungry = 100

    def eat(self, obj):
        if isinstance(obj, Predator):
            self._hungry += 20
            return
        self._hungry += 10

    def check_hp(self):
        return self.health_points > 0

    def starve(self):
        if self._hungry <= 0:
            self._hungry = 0
            self.health_points -= 5
        else:
            self._hungry -= 5

    def walk(self):
        ...

    @abstractmethod
    def make_move(self):
        pass

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
        return self._hungry

    @health_points.setter
    def health_points(self, value):
        if self._health_points + value > 100:
            self._health_points = 100
            return
        self._health_points += value

    def __str__(self):
        pass


class Predator(Creature):
    attack = 10
    speed = 2

    def __str__(self):
        return 'P'

    def make_move(self):
        pass

    def attack_creature(self, creature, map_obj):
        creature.health_points -= self.attack
        if not creature.check_hp():
            self.eat(creature)
            map_obj.delete_from_cell(*creature.position)


class Herbivore(Creature):
    speed = 2
    def make_move(self):
        pass

    def __str__(self):
        return 'H'


class Map:
    def __init__(self, n, m):
        self.size = (n, m)
        self.map_entities = {}

    def check_cell(self, x, y):
        return (x, y) not in self.map_entities

    def insert_in_cell(self, entity, x, y):
        if self.check_cell(x, y) and self.check_bounds(x, y):
            self.map_entities[(x, y)] = entity

    def delete_from_cell(self, x, y):
        if not self.check_cell(x, y):
            self.map_entities.pop((x, y))

    def get_entity_at(self, x, y):
        return self.map_entities[(x, y)] if not self.check_cell(x, y) and self.check_bounds(x, y) else None

    def check_bounds(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def create_map(self):
        a, b = self.size
        map_area = a * b

        balance = {
            'Grass': 0.2,
            'Rock': 0.05,
            'Tree': 0.07,
            'Predator': 0.05,
            'Herbivore': 0.1
        }

        entity_counts = {entity: int(map_area * proportion) for entity, proportion in balance.items()}

        for entity_class, count in entity_counts.items():
            for _ in range(count):
                while True:
                    x, y = random.randint(0, b - 1), random.randint(0, b - 1)
                    if self.check_cell(x, y):
                        self.insert_in_cell(eval(entity_class)(x, y), x, y)
                        break

    def move_entity(self, old_crds, new_crds):
        self.map_entities[new_crds] = self.map_entities.pop([old_crds])

class Renderer:
    def __init__(self, n, m):
        self.map = Map(n, m)
        self.map.create_map()

    def render_map(self):
        x, y = self.map.size
        for i in range(x):
            row = []
            for j in range(y):
                entity = self.map.map_entities.get((i, j))
                if entity:
                    row.append(str(entity))
                else:
                    row.append('.')
            print('  '.join(row))

a = Renderer(10, 10)
a.render_map()