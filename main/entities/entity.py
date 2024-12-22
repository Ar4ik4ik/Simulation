from abc import ABC, abstractmethod


class Entity(ABC):


    def __init__(self, x, y, map_instance):
        self.position = (x, y)
        self.map_instance = map_instance

    @abstractmethod
    def __repr__(self):
        pass

