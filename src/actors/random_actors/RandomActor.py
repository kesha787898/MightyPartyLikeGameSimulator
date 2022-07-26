import random
from typing import List

from src.abstract.AbstractActor import AbstractActor
from src.abstract.AbstractEnviroment import AbstractEnvironment
from src.abstract.AbstractHeroFactory import AbstractHeroFactory
from src.abstract.AbstractUnitFactory import AbstractUnitFactory


# Todo base Actor
class RandomActor(AbstractActor):
    def __init__(self, team_id: int, hero_factory: AbstractHeroFactory, units_factories: List[AbstractUnitFactory]):
        super().__init__()
        self.unit_factories = units_factories
        self.hero_factory = hero_factory
        self.team_id = team_id

    def place_hero(self, env: AbstractEnvironment) -> None:
        hero = self.hero_factory.create_hero(self.team_id)
        env.place_hero(hero)

    def place_unit(self, env: AbstractEnvironment) -> None:
        squares = env.get_map().get_free_squares(self.team_id)
        melee_squares = [square
                         for square in squares if
                         (square.get_x() == env.get_map().get_size_x() // 2 - 1 and self.team_id == 0) or
                         (square.get_x() == env.get_map().get_size_x() // 2 and self.team_id == 1)]
        range_squares = [square
                         for square in squares if
                         (square.get_x() != env.get_map().get_size_x() // 2 - 1 and self.team_id == 0) or
                         (square.get_x() != env.get_map().get_size_x() // 2 and self.team_id == 1)]

        units_ranged_factories = [factory for factory in self.unit_factories if factory.unit_type == 'ranged']
        units_melee_factories = [factory for factory in self.unit_factories if factory.unit_type == 'melee']

        available_units = []
        available_squares = []

        if melee_squares:
            available_units.append(units_melee_factories)
        if range_squares:
            available_squares.append(units_ranged_factories)
        if not available_squares:
            return
        square = random.choice(squares)
        if square in melee_squares:
            env.unit_placed(square.get_x(), square.get_y(),
                            random.choice(units_melee_factories).create_unit(self.team_id))
        elif square in range_squares:
            env.unit_placed(square.get_x(), square.get_y(),
                            random.choice(units_ranged_factories).create_unit(self.team_id))
        else:
            raise RuntimeError("unreachable code")

    def attack(self, env: AbstractEnvironment) -> None:
        env.user_attack(self.team_id)
