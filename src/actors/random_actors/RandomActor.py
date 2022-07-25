import random
from typing import List

from src.abstract.AbstractEnviroment import AbstractEnvironment
from src.abstract.AbstractActor import AbstractActor
from src.abstract.AbstractHeroFactory import AbstractHeroFactory
from src.abstract.AbstractUnitFactory import AbstractUnitFactory
from src.base.BaseUnit import MeleeUnit, RangedUnit


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
        if squares:
            # Todo!!!!!
            for i in range(10):
                square = random.choice(squares)
                # Todo
                if (square.get_x() == 3 and self.team_id == 0) or (square.get_x() == 4 and self.team_id == 1):
                    unit = random.choice(self.unit_factories).create_unit(self.team_id)
                    if isinstance(unit, MeleeUnit):
                        env.unit_placed(square.get_x(), square.get_y(), unit)
                        break
                else:
                    unit = random.choice(self.unit_factories).create_unit(self.team_id)
                    if isinstance(unit, RangedUnit):
                        env.unit_placed(square.get_x(), square.get_y(), unit)
                        break

    def attack(self, env: AbstractEnvironment) -> None:
        env.user_attack(self.team_id)
