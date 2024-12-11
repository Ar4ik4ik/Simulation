from main.path_finder.a_star import a_star

class Path:
    def __init__(self, map_instance):
        self._path = None
        self._map_instance = map_instance

    def find_nearest(self, self_position, ent_type):
        x, y = self_position
        closest_ent = None
        closest_dist = float('inf')

        for (ex, ey), entity in self._map_instance.map_entities.items():
            if isinstance(entity, ent_type) and self._map_instance.check_cell(ex, ey):  # Игнорируем занятые клетки
                distance = abs(ex - x) + abs(ey - y)
                if distance < closest_dist:
                    closest_dist = distance
                    closest_ent = entity
        return closest_ent

    def find_path(self, call_obj_position, food):
        nearest_food = self.find_nearest(call_obj_position, food)
        if nearest_food:
            self._path = a_star(call_obj_position, nearest_food.position, self._map_instance)