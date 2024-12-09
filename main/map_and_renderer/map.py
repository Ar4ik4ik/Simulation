import random
import json

from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator


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

        with open('balance_conf.json', 'r') as f:
            balance = json.load(f)

        entity_counts = {entity: int(map_area * proportion) for entity, proportion in balance.items()}
        for entity_class, count in entity_counts.items():
            for _ in range(count):
                while True:
                    x, y = random.randint(0, b - 1), random.randint(0, b - 1)
                    if self.check_cell(x, y):
                        entity_cls_eval = eval(entity_class)
                        entity = entity_cls_eval(x, y, self)
                        self.insert_in_cell(entity, x, y)
                        break

    def move_entity(self, old_crds, new_crds):
        self.map_entities[new_crds] = self.map_entities.pop(old_crds)

    def find_nearest(self, position, ent_type):
        x, y = position
        closest_ent = None
        closest_dist = float('inf')

        for (ex, ey), entity in self.map_entities.items():
            if isinstance(entity, ent_type) and self.check_cell(ex, ey):  # Игнорируем занятые клетки
                distance = abs(ex - x) + abs(ey - y)
                if distance < closest_dist:
                    closest_dist = distance
                    closest_ent = entity
        return closest_ent

    def get_creatures_list(self):
        obj_list = [ent for crds, ent in self.map_entities if isinstance(ent, (Predator, Herbivore))]
        return obj_list
