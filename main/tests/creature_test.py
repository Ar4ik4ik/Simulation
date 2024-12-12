import pytest

from main.entities.dynamic.herbivore import Herbivore
from main.entities.static import Grass

def test_move_to_method(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    assert map_instance.check_cell(0, 0) is False
    assert map_instance.check_cell(3, 3) is True
    creature.move_towards((3, 3))
    assert map_instance.check_cell(3, 3) is False
    assert map_instance.check_cell(0, 0) is True

def test_creature_moves_into_grass_and_restores_it(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    grass_3_3 = Grass(3, 3, map_instance)
    grass_4_3 = Grass(4, 3, map_instance)

    map_instance.insert_in_cell(grass_3_3, 3, 3)
    map_instance.insert_in_cell(grass_4_3, 4, 3)

    # Проверяем изначальное состояние
    assert isinstance(map_instance.get_entity_at(3, 3), Grass), "Initial grass at (3, 3) is missing."
    assert map_instance.check_cell(0, 0) is False, "Creature's initial position is unexpectedly empty."

    # Существо перемещается в клетку с травой
    creature.move_towards((3, 3))
    assert isinstance(map_instance.get_entity_at(3, 3), Herbivore), "Creature did not move to grass."
    assert map_instance.check_cell(0, 0) is True, "Creature's initial position is not empty after moving."

    # Существо перемещается в другую клетку с травой
    creature.move_towards((4, 3))
    assert isinstance(map_instance.get_entity_at(3, 3), Grass), "Grass at (3, 3) was not restored."
    assert isinstance(map_instance.get_entity_at(4, 3), Herbivore), "Creature did not move to (4, 3)."

    # Существо перемещается на пустую клетку
    creature.move_towards((4, 4))
    assert isinstance(map_instance.get_entity_at(4, 3), Grass), "Grass at (4, 3) was not restored."
    assert isinstance(map_instance.get_entity_at(4, 4), Herbivore), "Creature did not move to (4, 4)."

def test_random_move_method(one_creature_map):
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    creature.move_towards((3, 3))
    x, y = 3, 3
    creature.random_move()
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    assert creature.position in directions
