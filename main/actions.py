from main.map_and_renderer.renderer import Renderer, Map
from main.entities.static import Grass
from main.entities.dynamic.predator import Predator
from main.entities.dynamic.herbivore import Herbivore
from main.map_and_renderer.entity_generator import EntityGenerator


class Actions:

    def __init__(self, input_map: Map):
        self._map_instance = input_map
        self._renderer_obj = Renderer(self._map_instance)
        self._entity_generator_obj = EntityGenerator(self._map_instance)

    def init_map(self):
        self._entity_generator_obj.generate_entities()

    def grass_checker(self):
        """
        Проверяет и восстанавливает баланс травы на карте, если он нарушен.
        """
        a, b = self._map_instance.size
        total_cells_count = a * b
        grass_count = self._map_instance.get_entity_count(Grass)
        balance = self._map_instance.settings
        target_count = int(total_cells_count * balance['Grass'])

        if grass_count < target_count // 2:
            for _ in range(target_count - grass_count):
                try:
                    self._entity_generator_obj.generate_entity('Grass')
                except ValueError as e:
                    print(f"Не удалось создать сущность Grass: {e}")

    def turn_actions(self):
        """
        Выполняет действия всех существ на карте.
        Каждое существо делает ход в порядке его нахождения на карте.
        """
        creatures = self._map_instance.get_all_creatures_list(Herbivore, Predator)
        for creature in creatures:
            creature.make_move()

    def get_animals_count(self) -> dict[str, int]:
        """
        Возвращает количество травоядных и хищников на карте.

        Returns:
            dict[str, int]: Словарь с количеством существ.
        """
        herb = self._map_instance.get_entity_count(Herbivore)
        pred = self._map_instance.get_entity_count(Predator)
        return {'Herbivore': herb, 'Predator': pred}
