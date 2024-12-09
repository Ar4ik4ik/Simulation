from main.entities.entity import Entity

class Grass(Entity):
    def __str__(self):
        return 'G'


class Rock(Entity):
    def __str__(self):
        return 'R'


class Tree(Entity):
    def __str__(self):
        return 'T'
