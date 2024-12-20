from main.actions import Actions
from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator
from main.map_and_renderer.map import Map
from main.map_and_renderer.renderer import Renderer

class Simulation:

    def __init__(self, n: int, m: int):
        self.map_instance = Map(n, m)
        self.map_renderer = Renderer(self.map_instance)
        self.actions_controller = Actions(self.map_instance)
        self.turns_counter = 0

    def next_turn(self):
        if not self.map_instance.get_all_creatures_list(Herbivore, Predator):
            print(f"There are no entities in map obj, maybe you forgot init method")
        else:
            while True:
                if self.turns_counter % 15 == 0:
                    self.actions_controller.grass_checker()

                self.actions_controller.turn_actions()
                self.turns_counter += 1
                self.map_renderer.render_map()
                self.turns_counter_shower()
                self.entity_counter_shower()
                self.pause_simulation()

    def start_simulation(self):
        while True:
            if not self.map_instance.get_all_creatures_list(Predator):
                self.map_renderer.render_map()
                print(f"     Все хищники умерли с голоду")
                break

            elif not self.map_instance.get_all_creatures_list(Herbivore):
                self.map_renderer.render_map()
                print(f"     Все травоядные умерли с голоду")
                break

            if self.turns_counter % 15 == 0:
                self.actions_controller.grass_checker()
                self.map_renderer.render_map()
                self.turns_counter_shower()
                self.entity_counter_shower()
                self.pause_simulation()

            self.actions_controller.turn_actions()
            self.turns_counter += 1



    @staticmethod
    def pause_simulation():
        if not int(input("Нажмите '1' чтобы продолжить, '0' чтобы выйти \n")):
            print("Вы вышли из игры")
            exit()

    def turns_counter_shower(self):
        horizontal_border = "━" * self.map_renderer.line_len
        turns_str = f"Текущий ход: {self.turns_counter}"
        print(f"   ┃ {horizontal_border} ┃")
        print(f"   ┃{turns_str: ^{self.map_renderer.line_len}}  ┃")
        print(f"   ┃ {horizontal_border} ┃")

    def entity_counter_shower(self):
        horizontal_border = "━" * self.map_renderer.line_len
        animals_str = f"Количество животных"
        entities = self.actions_controller.get_animals_count()
        herb = f"Травоядные: {entities['Herbivore']}"
        pred = f"Хищники: {entities['Predator']}"
        print(f"   ┃ {horizontal_border} ┃\n"
              f"   ┃ {animals_str: ^{self.map_renderer.line_len}} ┃\n"
              f"   ┃ {herb: <{self.map_renderer.line_len}} ┃\n"
              f"   ┃ {pred: <{self.map_renderer.line_len}} ┃\n"
              f"   ┃ {horizontal_border} ┃")


    def get_history(self):
        ...


if __name__ == '__main__':
    s = Simulation(20, 20)
    s.actions_controller.init_map()
    s.start_simulation()








