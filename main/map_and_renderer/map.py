from main.entities.static import Grass

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

    def move_entity(self, old_crds, new_crds):
        self.map_entities[new_crds] = self.map_entities.pop(old_crds)

    def get_all_creatures_list(self, *creature):
        obj_list = [ent for crds, ent in self.map_entities.items() if isinstance(ent, creature)]
        return obj_list

    def get_entity_count(self, entity):
        return len([i for i, j in self.map_entities.items() if isinstance(j, entity)])

    def is_grass(self, x, y):
        return isinstance(self.get_entity_at(x, y), Grass)


if __name__ == '__main__':
    a = Map(5, 5)
    b = Herbivore(0, 0, a)
    a.insert_in_cell(b, 0, 0)
    print(a.get_all_creatures_list())
