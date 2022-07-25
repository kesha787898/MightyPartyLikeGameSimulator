from src.abstract.AbstractHero import AbstractHero


class AbstractHeroFactory:
    def create_hero(self, team_id: int) -> AbstractHero:
        raise NotImplementedError()
