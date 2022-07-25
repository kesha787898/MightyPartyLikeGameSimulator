# Todo it is base! not abstract
class AbstractUnitFactory:
    def __init__(self, fu):
        self.fu = fu

    def create_unit(self, team_id):
        return self.fu(team_id)
