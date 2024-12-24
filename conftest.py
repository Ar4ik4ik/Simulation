import pytest
from main.map_and_renderer.world_map import Map
from main.entities.static import Grass
from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator

@pytest.fixture
def empty_map():
    map_instance = Map(5, 5)
    return map_instance

@pytest.fixture
def non_empty_map():
    map_instance = Map(5, 5)
    a = Grass(0, 0, map_instance)
    map_instance.insert_in_cell(a, 0, 0)
    return map_instance

@pytest.fixture
def map_with_creatures():
    map_instance = Map(5, 5)
    for i in range(3):
        a = Herbivore(0 + i, 0, map_instance)
        b = Predator(0 + i, 1, map_instance)
        map_instance.insert_in_cell(a, 0 + i, 0)
        map_instance.insert_in_cell(b, 0 + i, 1)

    return map_instance

@pytest.fixture
def herb_predator_map():
    map_instance = Map(10, 10)
    a = Herbivore(2, 3, map_instance)
    b = Predator(7, 9, map_instance)
    return a, b, map_instance

@pytest.fixture
def one_creature_map():
    map_instance = Map(10, 10)
    a = Herbivore(0, 0, map_instance)
    map_instance.insert_in_cell(a, 0, 0)
    return a, map_instance
