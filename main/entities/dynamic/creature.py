from abc import abstractmethod
from main.entities.entity import Entity
from main.path_finder.path import Path
import random


class Creature(Entity):
    """
    Класс Creature представляет собой существо, которое может перемещаться по карте и взаимодействовать с едой.

    Атрибуты:
        x (int): Координата x существо на карте.
        y (int): Координата y существо на карте.
        map_instance (Map): Экземпляр карты, на которой находится существо.
        speed (int): Скорость существо.
        hp (int): Здоровье существо.
        attack (int): Атака существо.
        _health_points (int): Текущее здоровье существо.
        _hungry (int): Уровень голода существо.
        attack (int): Атака существо.
        speed (int): Скорость существо.
        max_health_points (int): Максимальное здоровье существо.
        path_obj (Path): Объект пути, используемый для поиска пути к еде.
    """

    def __init__(self, x, y, map_instance, speed, hp, attack):
        super().__init__(x, y, map_instance)
        self._health_points = hp
        self._hungry = 100
        self.attack = attack
        self.speed = speed
        self.max_health_points = hp
        self.path_obj = Path(map_instance)
        self.is_alive = True

    def check_hp(self):
        """
        Проверяет здоровье существо и удаляет его с карты, если оно меньше или равно нулю.
        """
        if self.health_points <= 0:
            self.map_instance.delete_from_cell(*self.position)
            self.is_alive = False

    def starve(self):
        """
        Уменьшает уровень голода существо на 2. Если уровень голода достигает 0, уменьшает здоровье существо на 2.
        """
        if self.hungry <= 0:
            self.hungry = 0
            self.health_points -= 2
        else:
            self.hungry -= 2

    @abstractmethod
    def interact_with_food(self, food):
        """
        Абстрактный метод, который должен быть реализован в подклассах для взаимодействия с едой.

        Параметры:
            food: Объект еды, с которой существо взаимодействует.
        """
        pass

    def make_move(self):
        """
        Определяет, что существо будет делать на следующем ходу. Если уровень голода меньше 50, ищет еду и движется к ней.
        Если еда не найдена, делает случайный ход. Если уровень голода больше или равен 50, увеличивает здоровье существо на 5 и делает случайный ход.
        """
        if self.hungry < 50:
            food_obj, food_dist = self.search_food().values()

            if food_dist == 1:
                self.interact_with_food(food_obj)
            elif food_obj:  # Тут проверяется что объект != None

                path = Path(self.map_instance)
                path = path.find_path(self.position, food_obj)
                if path:  # Если путь найден
                    if self.position == path[-1]:
                        self.interact_with_food(food_obj)
                        return
                    else:
                        target = path[min(self.speed, len(path) - 1)]
                        self.move_towards(target)
            else:
                self.random_move()
        else:
            self.health_points += 10
            self.random_move()
        self.starve()

    def random_move(self):
        """
        Делает случайный ход существо на карте.
        """
        x, y = self.position
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(directions)
        for nx, ny in directions:
            if self.map_instance.complex_check(nx, ny):
                self.move_towards((nx, ny))
                break

    def move_towards(self, target: tuple[int, int]):
        """
        Перемещает существо к указанной цели на карте.

        Параметры:
            target (tuple[int, int]): Координаты цели, к которой существо должно переместиться.
        """
        if self.map_instance.check_cell(*target) or self.map_instance.is_grass(*target):
            old_position = self.position
            self.map_instance.move_entity(old_position, target)
            self.position = target

    @abstractmethod
    def eat(self, obj):
        """
        Абстрактный метод, который должен быть реализован в подклассах для питания существо.

        Параметры:
            obj: Объект, который существо должно съесть.
        """
        pass

    @abstractmethod
    def search_food(self):
        """
        Абстрактный метод, который должен быть реализован в подклассах для поиска еды.

        Возвращает:
            dict: Словарь, содержащий объект еды и расстояние до него.
        """
        pass

    @property
    @abstractmethod
    def food_type(self):
        """
        Абстрактное свойство, которое должно быть реализовано в подклассах для определения типа еды, которую существо может есть.

        Возвращает:
            str: Тип еды, которую существо может есть.
        """
        pass

    @property
    def hungry(self):
        """
        Свойство, которое возвращает уровень голода существо.

        Возвращает:
            int: Уровень голода существо.
        """
        return self._hungry

    @hungry.setter
    def hungry(self, value: int):
        """
        Свойство, которое устанавливает уровень голода существо.

        Параметры:
            value (int): Новый уровень голода существо.
        """
        if value >= 100:
            self._hungry = 100

        elif value <= 0:
            self._hungry = 0

        else:
            self._hungry = value

    @property
    def health_points(self):
        """
        Свойство, которое возвращает текущее здоровье существо.

        Возвращает:
            int: Текущее здоровье существо.
        """
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value > self.max_health_points:
            self._health_points = self.max_health_points

        elif value <= 0:
            self._health_points = 0

        else:
            self._health_points = value

        self.check_hp()
