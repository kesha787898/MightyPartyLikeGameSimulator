from typing import List

from abstract.AbstractEnviroment import AbstractEnvironment
from src.abstract.AbstractHero import AbstractHero
from src.abstract.AbstractMap import AbstractMap
from src.abstract.AbstractUnit import AbstractUnit
from src.base.BaseHero import BaseHero
from src.base.BaseMap import BaseMap


class BaseEnvironment(AbstractEnvironment):

    def __init__(self):
        super().__init__()
        self.map = BaseMap(8, 4)
        self.units = []
        self.heroes = []
        self.status = 'not_started'
        self.winner = -1

    def place_hero(self, hero):
        self.heroes.append(hero)
        self.status = "started"

    def unit_placed(self, x, y, unit):
        self.map.place_unit(x, y)
        unit.on_placed(x, y)
        self.units.append(unit)

    def user_attack(self, team_id: int):
        for user_unit in self.get_user_units(user_id=team_id):
            # Todo think about abstract
            opps = user_unit.get_attacked_units(self.units, self.heroes)
            user_unit.attack(opps)
            for opp in opps:
                if not opp.is_alive():
                    if isinstance(opp, BaseHero) and not opp.is_alive():
                        self.status = "finished"
                        self.winner = team_id
                        break
                    else:
                        self.remove_unit(opp)

    def get_user_units(self, user_id: int):
        units = []
        for unit in self.units:
            if unit.team_id == user_id:
                units.append(unit)
        return units

    def remove_unit(self, unit: AbstractUnit):
        self.map.remove_unit(unit.x, unit.y)
        self.units.remove(unit)

    def get_enemy_hero(self, team_id: int) -> AbstractHero:
        return list(filter(lambda hero: hero.team_id != team_id, self.heroes))[0]

    def get_status(self) -> str:
        return self.status

    def get_map(self) -> AbstractMap:
        return self.map

    def get_heroes(self) -> List[AbstractHero]:
        return self.heroes

    def get_units(self) -> List[AbstractUnit]:
        return self.units
