from main.actions import Actions
from main.entities.dynamic.herbivore import Herbivore
from main.entities.dynamic.predator import Predator
from main.map_and_renderer.map import Map
from main.map_and_renderer.renderer import Renderer

class Simulation:

    def __init__(self, n, m):
        self.map_instance = Map(n, m)
        self.map_renderer = Renderer(self.map_instance)
        self.actions_controller = Actions(self.map_instance)
        self.turns_counter = 0

    def next_turn(self):
        if not self.map_instance.get_all_creatures_list(Herbivore, Predator):
            print(f"There are no entities in map obj, maybe you forgot init method")
        else:
            self.actions_controller.turn_actions()
            self.turns_counter += 1
            print(f"Ход {self.turns_counter}")

    def start_simulation(self):
        while True:
            if not self.map_instance.get_all_creatures_list(Predator):
                self.map_renderer.render_map()
                print(f"Все хищники умерли с голоду")
                break

            elif not self.map_instance.get_all_creatures_list(Herbivore):
                self.map_renderer.render_map()
                print(f"Все травоядные умерли с голоду")
                break

            if self.turns_counter % 15 == 0:
                self.map_renderer.render_map()
                print(f"Ход {self.turns_counter}")
                self.pause_simulation()

            self.actions_controller.turn_actions()
            self.turns_counter += 1



    @staticmethod
    def pause_simulation():
        if not int(input("Нажмите '1' чтобы продолжить, '0' чтобы выйти \n")):
            print("Вы вышли из игры")
            exit()

if __name__ == '__main__':
    s = Simulation(10, 8)
    s.actions_controller.init_map()
    s.start_simulation()








