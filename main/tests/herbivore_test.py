import pytest
from main.entities.dynamic.herbivore import Herbivore
from main.entities.static import Grass

def test_eat_method(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]

    g = Grass(0, 1, map_instance)
    map_instance.insert_in_cell(g, 0, 1)
    assert g.health_points == 2
    creature.eat(g)
    assert creature.hungry == 100
    assert g.health_points == 1
    creature.hungry = 50
    creature.eat(g)
    assert creature.hungry > 50
    assert g.health_points == 0
    assert g not in map_instance.map_entities
