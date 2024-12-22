import pytest

from conftest import map_with_creatures
from main.entities.dynamic.predator import Predator
from main.entities.dynamic.herbivore import Herbivore


def test_eat_method(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]

    p = Predator(1, 1, map_instance)
    map_instance.insert_in_cell(p, 1, 1)

    assert p in map_instance.map_entities.values()
    p.eat(creature)
    assert p.hungry == 100
    p.hungry = 50
    p.eat(creature)
    assert p.hungry == 70


def test_attack_method(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]

    p = Predator(1, 1, map_instance)
    map_instance.insert_in_cell(p, 1, 1)

    assert creature.health_points == creature.max_health_points
    p.interact_with_food(creature)
    assert creature.health_points == creature.max_health_points - p.attack


def test_attack_eat_methods(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]

    p = Predator(1, 1, map_instance)
    map_instance.insert_in_cell(p, 1, 1)

    p.hungry = 50
    p.interact_with_food(creature)
    p.interact_with_food(creature)
    p.interact_with_food(creature)
    p.interact_with_food(creature)
    assert p.hungry == 70
    assert creature not in map_instance.map_entities.values()