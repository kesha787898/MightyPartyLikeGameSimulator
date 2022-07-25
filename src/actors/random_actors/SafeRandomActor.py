import random

from abstract.AbstractEnviroment import AbstractEnvironment
from src.actors.random_actors.RandomActor import RandomActor


class SafeRandomActor(RandomActor):

    def place_unit(self, env: AbstractEnvironment):
        unit = random.choice(self.unit_factories).create_unit(self.team_id)
        squares = env.get_map().get_free_squares(unit.team_id)
        if squares:
            square = random.choice(squares)
            env.unit_placed(square.get_x(), square.get_y(), unit)
