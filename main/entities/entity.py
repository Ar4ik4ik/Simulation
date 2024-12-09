from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Базовый класс для всех объектов
    :param x: координата x
    :type x: int
    :param y: координата y
    :type y: int
    :param map_instance: экземпляр класса Map
    :type map_instance: class
    """

    def __init__(self, x, y, map_instance):
        self.position = (x, y)
        self.map_instance = map_instance

    @abstractmethod
    def __repr__(self):
        pass
