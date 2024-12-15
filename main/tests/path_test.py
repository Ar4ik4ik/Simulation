import pytest
from main.entities.static import Grass

def test_find_nearest_obj(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    a = Grass(0, 5, map_instance)
    map_instance.insert_in_cell(a, 0, 5)
    assert creature.path_obj.find_nearest((0, 0), Grass) == a
    b = Grass(0, 4, map_instance)
    map_instance.insert_in_cell(b, 0, 4)
    assert creature.path_obj.find_nearest((0, 0), Grass) == b


def test_path_getter(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    a = Grass(0, 5, map_instance)
    map_instance.insert_in_cell(a, 0, 5)
    b = Grass(0, 4, map_instance)
    map_instance.insert_in_cell(b, 0, 4)
    assert creature.path_obj.find_path(call_obj_position=creature.position, food=Grass) is False
