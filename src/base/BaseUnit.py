import warnings
from typing import List

from src.abstract.AbstractUnit import AbstractUnit


class BaseUnit(AbstractUnit):
    def __init__(self, team_id: int, hp: int, base_attack_power: int, name: str):
        super().__init__(hp)
        self.team_id = team_id
        self.base_attack_power = base_attack_power
        self.name = name
        self.type = None

    def attack(self, units: List[AbstractUnit]):
        for unit in units:
            unit.on_attacked(self)

    def __str__(self) -> str:
        return f"id = {self.id}, " \
               f"hp = {self.hp}," \
               f"attack={self.base_attack_power}," \
               f"team={self.team_id}," \
               f" pos_x={self.x}," \
               f"pos_y={self.y}"

    def __repr__(self):
        return str(self) + '\n'


class RangedUnit(BaseUnit):

    def __init__(self, team_id: int, hp: int, base_attack_power: int, name: str):
        super().__init__(team_id, hp, base_attack_power, name)
        self.type = "Ranged"

    def get_attacked_units(self, all_units, heroes) -> List[AbstractUnit]:
        units_on_line = [i for i in filter(lambda unit: unit.y == self.y, all_units)]
        opps_on_line = list(filter(lambda unit: unit.team_id != self.team_id, units_on_line))
        opps = sorted(opps_on_line, key=lambda opp: opp.x)
        if not opps:
            opp_hero = [hero for hero in heroes if hero.team_id != self.team_id][0]
            return [opp_hero]
        elif self.team_id == 0:
            return [opps[0]]
        elif self.team_id == 1:
            return [opps[-1]]
        else:
            warnings.warn("unreachable code")
            return []


class MeleeUnit(BaseUnit):

    def __init__(self, team_id: int, hp: int, base_attack_power: int, name: str):
        super().__init__(team_id, hp, base_attack_power, name)
        self.type = "Melee"

    def get_attacked_units(self, all_units, heroes) -> List[AbstractUnit]:
        units_on_line = [i for i in filter(lambda unit: unit.y == self.y, all_units)]
        opps_on_line = list(filter(lambda unit: unit.team_id != self.team_id, units_on_line))
        friend_units = list(filter(lambda unit: unit.team_id == self.team_id, units_on_line))
        opps = sorted(opps_on_line, key=lambda opp: opp.x)
        if not opps:
            opp_hero = [hero for hero in heroes if hero.team_id != self.team_id][0]
            return [opp_hero]
        elif self.team_id == 0:
            if friend_units and friend_units[-1].x > self.x:
                return []
            else:
                return [opps[0]]
        elif self.team_id == 1:
            if friend_units and friend_units[0].x < self.x:
                return []
            else:
                return [opps[-1]]
        else:
            return []
