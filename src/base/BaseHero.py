from src.abstract.AbstractHero import AbstractHero


class BaseHero(AbstractHero):
    def __init__(self, hp: int, team_id: int):
        super().__init__(hp)
        self.team_id = team_id

    def __str__(self) -> str:
        return f"hp = {self.hp},team={self.team_id}"

    def __repr__(self):
        return str(self) + '\n'
