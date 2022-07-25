from typing import List

from src.abstract.AbstractHero import AbstractHero
from src.abstract.AbstractMap import AbstractMap
from src.abstract.AbstractUnit import AbstractUnit


class AbstractEnvironment:
    def place_hero(self, hero: AbstractHero):
        raise NotImplementedError()

    def unit_placed(self, x: int, y: int, unit: AbstractUnit):
        raise NotImplementedError()

    def user_attack(self, team_id: int):
        raise NotImplementedError()

    def get_user_units(self, user_id: int) -> List[AbstractUnit]:
        raise NotImplementedError()

    def remove_unit(self, unit: AbstractUnit):
        raise NotImplementedError()

    def get_enemy_hero(self, team_id: int) -> AbstractHero:
        raise NotImplementedError()

    # Todo enum statuses
    def get_status(self) -> str:
        raise NotImplementedError()

    def get_map(self) -> AbstractMap:
        raise NotImplementedError()

    def get_heroes(self) -> List[AbstractHero]:
        raise NotImplementedError()

    def get_units(self) -> List[AbstractUnit]:
        raise NotImplementedError()

    # Todo maybe in base?
    def __str__(self) -> str:
        res = ""
        res += f"status ={self.get_status()}\n"
        res += "map:\n"
        res += str(self.get_map())
        res += "heroes\n"
        res += str(self.get_heroes())
        res += "\nunits:\n"
        res += str(self.get_units())
        return res
