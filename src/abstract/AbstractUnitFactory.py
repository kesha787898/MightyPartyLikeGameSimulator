from abstract.AbstractUnit import AbstractUnit


# Todo it is base! not abstract
class AbstractUnitFactory:
    def __init__(self, fu, unit_type: str):
        self.unit_type = unit_type
        self.fu = fu

    def create_unit(self, team_id: int) -> AbstractUnit:
        unit = self.fu(team_id)
        unit.unit_type = self.unit_type
        return unit
