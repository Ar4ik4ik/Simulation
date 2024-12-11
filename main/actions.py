from map_and_renderer.renderer import Renderer, Map
from entities.static import Grass, Rock, Tree
from entities.dynamic.predator import Predator
from entities.dynamic.herbivore import Herbivore
import json
import random


class Actions:

    def __init__(self, n, m):
        self._map_instance = Map(n, m)
        self._renderer_obj = Renderer(self._map_instance)

    def init_map(self):
        a, b = self._map_instance.size
        map_area = a * b

        with open('balance_conf.json', 'r') as f:
            balance = json.load(f)

        entity_counts = {entity: int(map_area * proportion) for entity, proportion in balance.items()}
        for entity_class, count in entity_counts.items():
            for _ in range(count):
                while True:
                    x, y = random.randint(0, b - 1), random.randint(0, b - 1)
                    if self._map_instance.check_cell(x, y):
                        entity_cls_eval = eval(entity_class)
                        entity = entity_cls_eval(x, y, self)
                        self._map_instance.insert_in_cell(entity, x, y)
                        break

    def grass_checker(self):
        a, b = self._map_instance.size
        total_cells_count = a * b
        grass_count = self._map_instance.get_entity_count(Grass)

        with open('balance_conf.json', 'r') as f:
            balance = json.load(f)
        target_count = int(total_cells_count * balance['Grass'])

        if grass_count < target_count:
            for i in range(target_count - grass_count):
                while True:
                    x, y = random.randint(0, b - 1), random.randint(0, b - 1)
                    if self._map_instance.check_cell(x, y):
                        self._map_instance.insert_in_cell(Grass, x, y)
                        break

    def turn_actions(self):
        for creature in self._map_instance.get_all_creatures_list(Herbivore, Predator):
            if creature in self._map_instance.get_all_creatures_list(Herbivore, Predator):
                creature.make_move()
        self._renderer_obj.render_map()


if __name__ == '__main__':
    a = Actions(10, 10)
    print(a._map_instance.map_entities)
    a.init_map()
    a.turn_actions()
    a.turn_actions()
    a.turn_actions()
    a.turn_actions()
