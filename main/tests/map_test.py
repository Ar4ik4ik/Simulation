from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator
from main.entities.static import Grass


def test_empty_map_after_creation(empty_map):
    """Проверяет, что после создания экземпляра класса Map, все ячейки пустые"""
    assert empty_map.check_cell(3, 3) is True


def test_check_bounds_fn(empty_map):
    assert empty_map.check_bounds(0, 0) is True
    assert empty_map.check_bounds(4, 4) is True
    assert empty_map.check_bounds(5, 4) is False
    assert empty_map.check_bounds(4, 5) is False
    assert empty_map.check_bounds(4, -5) is False


def test_check_cell_before_insert(empty_map):
    """Проверяет, что после использования метода вставки, объект находится в ячейке"""
    assert empty_map.check_cell(3, 2) is True


def test_check_cell_after_insert(empty_map):
    """Проверяет, что после использования метода вставки, объект находится в ячейке"""
    empty_map.insert_in_cell(Grass, 3, 2)
    assert empty_map.check_cell(3, 2) is False


def test_delete_from_cell_method(non_empty_map):
    """Метод удаления объекта из ячейки"""
    assert non_empty_map.check_cell(0, 0) is False
    non_empty_map.delete_from_cell(0, 0)
    assert non_empty_map.check_cell(0, 0) is True


def test_entity_getter(non_empty_map):
    """Геттер для объекта в словаре экземпляра карты"""
    assert type(non_empty_map.get_entity_at(0, 0)) is Grass


def test_move_method(non_empty_map):
    """Метод для перестановки объекта на карте"""
    non_empty_map.move_entity((0, 0), (3, 2))
    assert non_empty_map.check_cell(3, 2) is False
    assert non_empty_map.check_cell(0, 0) is True


def test_grass_checker_method(non_empty_map):
    """Метод is_grass. True если объект == type(Grass)"""
    assert non_empty_map.is_grass(0, 0) is True


def test_get_creature_list_method(map_with_creatures):
    """Метод для возврата всех экземпляров Creature на карте"""
    creature_types = [type(i) for i in map_with_creatures.get_all_creatures_list(Predator, Herbivore)]
    assert Predator in creature_types
    assert Herbivore in creature_types


def test_get_ent_count_method(map_with_creatures):
    """Метод для пересчета общего количества динамических существ на карте"""
    assert len(map_with_creatures.get_all_creatures_list(Predator, Herbivore)) == 6

def test_complex_check_method(one_creature_map):
    """Метод для комплексной проверки"""
    creature = one_creature_map[0]
    map_instance = one_creature_map[1]
    assert map_instance.complex_check(1, 1) is True
