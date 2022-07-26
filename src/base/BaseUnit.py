from typing import List

from src.abstract.AbstractUnit import AbstractUnit


class BaseUnit(AbstractUnit):
    def __init__(self, team_id: int, hp: int, base_attack_power: int, name: str):
        super().__init__(hp)
        self.team_id = team_id
        self.base_attack_power = base_attack_power
        self.name = name
        self.unit_type = None

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

    def get_attacked_units(self, all_units: List[AbstractUnit], heroes) -> List[AbstractUnit]:
        units_on_line = sorted([i for i in filter(lambda unit: unit.y == self.y, all_units)], key=lambda unit: unit.x)
        opps_on_line = list(filter(lambda unit: unit.team_id != self.team_id, units_on_line))
        friend_units = list(filter(lambda unit: unit.team_id == self.team_id, units_on_line))
        if not opps_on_line:
            opp_hero = [hero for hero in heroes if hero.team_id != self.team_id][0]
            return [opp_hero]
        elif self.unit_type == "ranged":
            return [opps_on_line[0]]
        elif self.unit_type == "melee":
            if self.team_id == 0:
                if friend_units and friend_units[-1].x > self.x:
                    return []
                else:
                    return [opps_on_line[0]]
            elif self.team_id == 1:
                if friend_units and friend_units[0].x < self.x:
                    return []
                else:
                    return [opps_on_line[-1]]
            else:
                raise RuntimeError("unreachable code")
        else:
            raise RuntimeError("unreachable code")
