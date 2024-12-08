from abc import ABC, abstractmethod
import random
import a_star


class Entity(ABC):
    """
    Базовый класс для всех объектов
    :param x: координата x
    :type x: int
    :param y: координата y
    :type y: int
    :param map_instance: экземпляр класса Map
    :type map_instance: class
    """
    def __init__(self, x, y, map_instance):
        self.position = (x, y)
        self.map_instance = map_instance

    @abstractmethod
    def __str__(self):
        pass


class Grass(Entity):
    def __str__(self):
        return 'G'


class Rock(Entity):
    def __str__(self):
        return 'R'


class Tree(Entity):
    def __str__(self):
        return 'T'


class Creature(Entity):
    def __init__(self, x, y, map_instance):
        super().__init__(x, y, map_instance)
        self._health_points = 100
        self._hungry = 100

    def eat(self, obj):
        if isinstance(self, Predator):
            self._hungry += 20
            obj.map_instance.delete_from_cell(*obj.position)
            return
        self._hungry += 10
        obj.map_instance.delete_from_cell(*obj.position)

    # Метод, который будет вызываться каждый ход, для отслеживания состояний сущностей
    def check_hp(self):
        if self._health_points <= 0:
            self.map_instance.delete_from_cell(*self.position)

    # Метод, который используется в проверке, если не ест, то голодает и идет к еде
    def starve(self):
        if self._hungry <= 0:
            self._hungry = 0
            self.health_points -= 5
        else:
            self._hungry -= 5

    def move_entity(self, new_x, new_y):
        if self.map_instance.check_bounds(new_x, new_y) and self.map_instance.check_cell(new_x, new_y):
            old_position = self.position
            self.position = (new_x, new_y)
            self.map_instance.move_entity(new_x, new_y)

    @abstractmethod
    def search_food(self):
        pass

    def random_move(self):
        x, y = self.position
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(directions)

        for nx, ny in directions:
            if self.map_instance.check_bounds(nx, ny) and self.map_instance.check_cell(nx, ny):
                self.move_towards((nx, ny))
                break

    def make_move(self):
        if self._hungry < 50:
            food_position = self.search_food()
            if food_position:
                path = a_star.a_star(self.position, food_position, self.map_instance)
                if path:  # Если путь найден
                    self.move_towards(path[1])
            else:
                self.random_move()
        else:
            self.random_move()

    def move_towards(self, target):
        if self.map_instance.check_cell(*target):
            old_position = self.position
            self.position = target
            self.map_instance.move_entity(old_position, target)

    @property
    def hungry(self):
        return self._hungry

    @hungry.setter
    def hungry(self, value):
        if self._hungry + value >= 100:
            self._hungry = 100
            return
        self._hungry += value

    @property
    def health_points(self):
        return self._hungry

    @health_points.setter
    def health_points(self, value):
        if self._health_points + value > 100:
            self._health_points = 100
            return
        self._health_points += value
        self.check_hp()

    def __str__(self):
        return 'C'


class Predator(Creature):
    attack = 10
    speed = 2

    def __str__(self):
        return 'P'

    def search_food(self):
        target_entity = self.map_instance.find_nearest(self.position, Herbivore)
        return target_entity.position if target_entity else None

    def attack_creature(self, creature, map_obj):
        creature.health_points -= self.attack
        if not creature.check_hp():
            self.eat(creature)


class Herbivore(Creature):
    speed = 2

    def search_food(self):
        target = self.map_instance.find_neares(self.position, Grass)
        if target:
            self.move_towards(target.position)
        else:
            self.random_move()

    def __str__(self):
        return 'H'
