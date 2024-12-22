from main.map_and_renderer.map import Map
from main.path_finder.a_star import a_star, get_neighbors, heuristic
from main.entities.static import Grass

class Path:
    def __init__(self, map_instance: Map):
        self._path = None
        self._map_instance = map_instance

    def find_nearest(self, self_position: tuple[int, int], ent_type: type[Grass] | type) -> dict[str, type[Grass] | int]:
        x, y = self_position
        closest_ent = None
        closest_dist = float('inf')

        for (ex, ey), entity in self._map_instance.map_entities.items():
            if isinstance(entity, ent_type):
                distance = abs(ex - x) + abs(ey - y)
                if distance < closest_dist:
                    closest_dist = distance
                    closest_ent = entity
                    if closest_dist == 1:
                        break
        return {'closest_ent': closest_ent, 'closest_dist': closest_dist}

    def find_path(self, call_obj_position: tuple[int, int], food: type) -> list[tuple[int, int]]:
        # Ищем соседние клетки рядом с едой
        neighbors = get_neighbors(food.position, self._map_instance)
        sorted_neighbors = sorted(neighbors, key=lambda n: heuristic(call_obj_position, n[0]))
        for neighbor, weight in sorted_neighbors:
            if self._map_instance.check_cell(*neighbor):  # Пустая соседняя клетка
                path = a_star(call_obj_position, neighbor, self._map_instance)
                if path:
                    return path[1:]
        return []


