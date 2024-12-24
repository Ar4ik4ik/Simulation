import pytest

from main.entities.dynamic.herbivore import Herbivore
from main.entities.static import Grass
from main.map_and_renderer.world_map import Map
from main.path_finder.a_star import a_star


def test_find_nearest_obj(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    a = Grass(0, 5, map_instance)
    map_instance.insert_in_cell(a, 0, 5)
    assert id(creature.path_obj.find_nearest((0, 0), Grass)['closest_ent']) == id(a)
    b = Grass(0, 4, map_instance)
    map_instance.insert_in_cell(b, 0, 4)
    assert id(creature.path_obj.find_nearest((0, 0), Grass)['closest_ent']) == id(b)


def test_path_getter(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    a = Grass(0, 5, map_instance)
    map_instance.insert_in_cell(a, 0, 5)
    b = Grass(0, 4, map_instance)
    map_instance.insert_in_cell(b, 0, 4)
    assert creature.path_obj.find_path(call_obj_position=creature.position,
                                       food=creature.path_obj.find_nearest(creature.position, Grass)[
                                           'closest_ent']) is not None or False, "Path getter isn't working"


def test_a_star_on_simple_map():
    map_instance = Map(5, 5)
    map_instance.insert_in_cell(Grass(1, 1, map_instance), 1, 1)
    map_instance.insert_in_cell(Grass(1, 2, map_instance), 1, 2)
    start = (0, 0)
    target = (2, 2)

    path = a_star(start, target, map_instance)

    assert path == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], "Incorrect path"


def test_path_building_with_herbivore():
    map_instance = Map(5, 5)
    map_instance.insert_in_cell(Grass(1, 1, map_instance), 1, 1)
    map_instance.insert_in_cell(Grass(1, 2, map_instance), 1, 2)
    a = Herbivore(0, 0, map_instance)
    map_instance.insert_in_cell(a, 0, 0)
    path = a.path_obj.find_path(a.position, a.path_obj.find_nearest((0, 0), Grass)['closest_ent'])
    assert path == [(0, 1)], "Incorrect path"
