from typing import List

from src.abstract.RenameMe import MapObject, AliveObject, WithId


class AbstractUnit(AliveObject, MapObject, WithId):
    def __init__(self, hp: int):
        super().__init__(hp)

    # Todo annot
    def attack(self, units: List):
        raise NotImplementedError()

    # Todo it is not unit it is hero too
    def get_attacked_units(self, units, heroes):
        raise NotImplementedError()

