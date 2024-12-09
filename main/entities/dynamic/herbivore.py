class Herbivore(Creature):
    speed = 2

    def search_food(self):
        target = self.map_instance.find_neares(self.position, Grass)
        if target:
            self.move_towards(target.position)
        else:
            self.random_move()

    def __str__(self):
        return 'H'
