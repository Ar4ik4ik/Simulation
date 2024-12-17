from main.entities.static import Grass
import os
import json

class Map:

    def __init__(self, n: int, m: int):
        self.size = (n, m)
        self.map_entities = {}
        self._temporary_grass_obj = {}
        config_path = os.path.join(os.path.dirname(__file__), 'balance_conf.json')
        with open(config_path, 'r') as f:
            balance = json.load(f)
        self._settings = balance

    def check_cell(self, x: int, y: int) -> bool:
        return (x, y) not in self.map_entities

    def insert_in_cell(self, entity: type, x: int, y: int):
        if self.check_cell(x, y) and self.check_bounds(x, y):
            self.map_entities[(x, y)] = entity

    def delete_from_cell(self, x: int, y: int):
        if not self.check_cell(x, y):
            ent = self.map_entities.pop((x, y))
            print(f"Убран {ent.__class__.__name__}")

    def get_entity_at(self, x: int, y: int) -> bool:
        return self.map_entities[(x, y)] if not self.check_cell(x, y) and self.check_bounds(x, y) else None

    def check_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def move_entity(self, old_crds: tuple[int, int], new_crds: tuple[int, int]):
        # Если новая ячейка пуста
        if not self.map_entities.get(new_crds, None):
            # Если в старой ячейке была временно сохранённая трава
            if old_crds in self._temporary_grass_obj:
                self.map_entities[new_crds] = self.map_entities.pop(old_crds)
                self.map_entities[old_crds] = self._temporary_grass_obj.pop(old_crds)
            else:
                self.map_entities[new_crds] = self.map_entities.pop(old_crds)

        # Если в новой ячейке Grass
        elif isinstance(self.map_entities.get(new_crds), Grass):
            # Сохраняем текущий Grass во временный словарь
            self._temporary_grass_obj[new_crds] = self.map_entities[new_crds]
            self.map_entities[new_crds] = self.map_entities.pop(old_crds)

            # Если старая ячейка содержала временный Grass, восстанавливаем его
            if old_crds in self._temporary_grass_obj:
                self.map_entities[old_crds] = self._temporary_grass_obj.pop(old_crds)

    def get_all_creatures_list(self, *creature) -> list:
        obj_list = [ent for crds, ent in self.map_entities.items() if isinstance(ent, creature)]
        return obj_list

    def get_entity_count(self, entity: type) -> int:
        return len([i for i, j in self.map_entities.items() if isinstance(j, entity)])

    def is_grass(self, x: int, y: int) -> bool:
        return isinstance(self.get_entity_at(x, y), Grass)

    def is_static(self, x: int, y: int) -> bool:
        from main.entities.static import Rock
        from main.entities.static import Tree
        return isinstance(self.get_entity_at(x, y), (Rock, Tree))

    def complex_check(self, x: int, y: int) -> bool:
        return (self.check_bounds(x, y)
                and self.check_cell(x, y)
                and not self.is_grass(x, y))

    @property
    def settings(self):
        return self._settings
