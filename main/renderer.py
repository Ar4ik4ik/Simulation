class Renderer:
    """
    Класс для рендера карты, принимает экземпляр класса карты
    :param map_instance: Экземпляр класса Map
    """
    def __init__(self, map_instance):
        self.map = map_instance
        self.map.create_map()

    def render_map(self):
        """
        Метод для отрисовки состояния карты,
        проход по каждому ключу в словаре
        :return:
        """
        x, y = self.map.size
        for i in range(x):
            row = []
            for j in range(y):
                entity = self.map.map_entities.get((i, j))
                if entity:
                    row.append(str(entity))
                else:
                    row.append('.')
            print('  '.join(row))
