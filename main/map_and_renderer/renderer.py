import os
from main.map_and_renderer.map import Map


class Renderer:
    """
    Класс для рендера карты, принимает экземпляр класса карты
    :param map_instance: Экземпляр класса Map
    """

    def __init__(self, map_instance: Map):
        self._map = map_instance
        self.move_counter = 0
        self.line_len = None

    def render_map(self):
        self.clear_console()

        x, y = self._map.size
        rows = []

        for i in range(x):
            row = []
            for j in range(y):
                entity = self._map.get_entity_at(i, j)
                if entity:
                    emoji = str(entity)
                else:
                    emoji = '⬜'
                row.append(emoji)
            rows.append(row)

        # Верхняя и нижняя границы
        horizontal_border = "━" * (y * 3)
        self.line_len = len(horizontal_border)
        print(" " * 5 + horizontal_border)
        for row in rows:
            line = " ".join(row)
            print(f"   ┃ {line} ┃")
        print(" " * 5 + horizontal_border)

    @staticmethod
    def clear_console():
        os.system('cls')
        print('\n')
