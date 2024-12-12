import os
from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator
from main.map_and_renderer.map import Map
from wcwidth import wcswidth

class Renderer:
    """
    Класс для рендера карты, принимает экземпляр класса карты
    :param map_instance: Экземпляр класса Map
    """

    def __init__(self, map_instance):
        self._map = map_instance
        self.move_counter = 0

    def render_map(self):
        x, y = self._map.size
        max_width = 0
        rows = []

        for i in range(x):
            row = []
            for j in range(y):
                entity = self._map.map_entities.get((i, j))
                if entity:
                    emoji = str(entity)
                else:
                    emoji = '⬜'
                row.append(emoji)
            rows.append(row)

        max_width = max(wcswidth(" ".join(row)) for row in rows)
        print('\n')
        for row in rows:
            line = " ".join(row)
            padding = (max_width - wcswidth(line)) // 2
            print(" " * 5 + line)
        print('\n')

        self.increase_counter()

    def increase_counter(self):
        self.move_counter += 1

    def count_animals(self):
        all_animals = len(self._map.get_creatures_list())
        herb = len(self._map.get_creatures_list(creature=Herbivore))
        predator = len(self._map.get_creatures_list(creature=Predator))

    @staticmethod
    def clear_console():
        os.system('clear')
