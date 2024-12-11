from main.entities.entity import Entity

class Grass(Entity):
    def __init__(self, x, y, map_instance):
        super().__init__(x, y, map_instance)
        self.hp = 2

    def __repr__(self):
        return "🟩"


class Rock(Entity):
    def __repr__(self):
        return "⬛"


class Tree(Entity):
    def __repr__(self):
        return "🟫"
