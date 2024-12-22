import random
from main.entities.static import Grass, Rock, Tree
from main.entities.dynamic.predator import Predator
from main.entities.dynamic.herbivore import Herbivore


class EntityGenerator:

    def __init__(self, map_instance):
        self._map_instance = map_instance

    def calc_balance(self):
        """
        Генерирует название сущности и количество объектов на карте.
        """
        a, b = self._map_instance.size
        map_area = a * b
        for entity, proportion in self._map_instance.settings.items():
            yield entity, int(map_area * proportion)

    def generate_entity(self, entity_cls: str):
        a, b = self._map_instance.size
        for _ in range(25):
            x, y = random.randint(0, b - 1), random.randint(0, b - 1)
            if self._map_instance.check_cell(x, y):
                entity_cls_eval = eval(entity_cls)
                entity = entity_cls_eval(x, y, self._map_instance)
                self._map_instance.insert_in_cell(entity, x, y)
                return True
        print(f"Failed to place entity {entity_cls} after 25 attempts.")
        return False

    def generate_entities(self):
        for entity_class, count in self.calc_balance():
            for _ in range(count):
                self.generate_entity(entity_class)
        return