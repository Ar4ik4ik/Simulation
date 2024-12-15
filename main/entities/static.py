from main.entities.entity import Entity

class Grass(Entity):
    def __init__(self, x, y, map_instance):
        super().__init__(x, y, map_instance)
        self.health_points = 2

    def check_hp(self):
        if self.health_points <= 0:
            self.map_instance.delete_from_cell(*self.position)

    def __repr__(self):
        return "🟩"


class Rock(Entity):
    def __repr__(self):
        return "⬛"


class Tree(Entity):
    def __repr__(self):
        return "🟫"
