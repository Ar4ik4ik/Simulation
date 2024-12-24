from main.actions import Actions
from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator
from main.map_and_renderer.world_map import Map
from main.map_and_renderer.renderer import Renderer

class Simulation:

    def __init__(self):
        self._map_instance = Map()
        self._map_renderer = Renderer(self._map_instance)
        self._actions_controller = Actions(self._map_instance)
        self.turns_counter = 0

    def next_turn(self):
        if not self._map_instance.get_all_creatures_list(Herbivore, Predator):
            print(f"There are no entities in map obj, maybe you forgot init method")
        else:
            while True:
                self.execute_turn()

    def start_simulation(self):
        while True:
            if not self._map_instance.get_all_creatures_list(Predator):
                self._map_renderer.render_map()
                print(f"     Все хищники умерли с голоду")
                self.restart_simulation()
                break

            elif not self._map_instance.get_all_creatures_list(Herbivore):
                self._map_renderer.render_map()
                print(f"     Все травоядные умерли с голоду")
                self.restart_simulation()
                break

            else:
                for i in range(15):
                    self.execute_turn(True)
                self.pause_simulation()

    def execute_turn(self, cycle=False):
        if self.turns_counter % 15 == 0:
            self._actions_controller.grass_checker()

        self._actions_controller.turn_actions()
        self.turns_counter += 1
        if not cycle:
            self._map_renderer.render_map()
            self.display_turn_count()
            self.display_entity_count()
            if not self.pause_simulation():
                exit()
            else:
                self.execute_turn()
        else:
            if self.turns_counter % 15 == 0:
                self._map_renderer.render_map()
                self.display_turn_count()
                self.display_entity_count()

    @staticmethod
    def pause_simulation() -> bool:
        while True:
            try:
                choice = int(input("Нажмите '1' чтобы продолжить, '0' чтобы выйти \n"))
                if choice in (0, 1):
                    break
                print("Неверный ввод. Введите '1' или '0'.")
            except ValueError:
                print("Пожалуйста, введите число.")
        if choice == 0:
            print("Вы вышли из игры")
            exit()
        return True

    def restart_simulation(self):
        while True:
            try:
                choice = int(input("Нажмите '1' чтобы начать новую игру, '0' чтобы выйти \n"))
                if choice in (0, 1):
                    break
                print("Неверный ввод. Введите '1' или '0'.")
            except ValueError:
                print("Пожалуйста, введите число.")
        if choice == 0:
            print("Вы вышли из игры")
            return False

        self._map_instance.reset_map()
        self._actions_controller.init_map()
        self.turns_counter = 0

        s.start_simulation()

        return True


    def display_turn_count(self):
        horizontal_border = "━" * self._map_renderer.line_len
        turns_str = f"Текущий ход: {self.turns_counter}"
        print(f"   ┃ {horizontal_border} ┃")
        print(f"   ┃{turns_str: ^{self._map_renderer.line_len}}  ┃")
        print(f"   ┃ {horizontal_border} ┃")

    def display_entity_count(self):
        horizontal_border = "━" * self._map_renderer.line_len
        animals_str = f"Количество животных"
        entities = self._actions_controller.get_animals_count()
        herbivore_count = f"Травоядные: {entities['Herbivore']}"
        predator_count = f"Хищники: {entities['Predator']}"
        print(f"   ┃ {horizontal_border} ┃\n"
              f"   ┃ {animals_str: ^{self._map_renderer.line_len}} ┃\n"
              f"   ┃ {herbivore_count: <{self._map_renderer.line_len}} ┃\n"
              f"   ┃ {predator_count: <{self._map_renderer.line_len}} ┃\n"
              f"   ┃ {horizontal_border} ┃")


if __name__ == '__main__':
    s = Simulation()
    s._actions_controller.init_map()
    s.start_simulation()
