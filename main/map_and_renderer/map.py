from main.entities.static import Grass


class Map:

    def __init__(self, n, m):
        self.size = (n, m)
        self.map_entities = {}
        self._temporary_grass_obj = {}

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

    def move_entity(self, old_crds, new_crds):
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

    def get_all_creatures_list(self, *creature):
        obj_list = [ent for crds, ent in self.map_entities.items() if isinstance(ent, creature)]
        return obj_list

    def get_entity_count(self, entity):
        return len([i for i, j in self.map_entities.items() if isinstance(j, entity)])

    def is_grass(self, x, y):
        from main.entities.static import Grass
        return isinstance(self.get_entity_at(x, y), Grass)

    def complex_check(self, x, y):
        return (self.check_bounds(x, y)
                and self.check_cell(x, y)
                and not self.is_grass(x, y))
