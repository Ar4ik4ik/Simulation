class Predator(Creature):
    attack = 10
    speed = 2

    def __str__(self):
        return 'P'

    def search_food(self):
        target_entity = self.map_instance.find_nearest(self.position, Herbivore)
        return target_entity.position if target_entity else None

    def attack_creature(self, creature, map_obj):
        creature.health_points -= self.attack
        if not creature.check_hp():
            self.eat(creature)