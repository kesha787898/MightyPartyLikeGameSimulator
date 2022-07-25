from src.abstract.AbstractHeroFactory import AbstractHeroFactory
from src.base.BaseHero import BaseHero


class OnlyHpHeroFactory(AbstractHeroFactory):
    def __init__(self, hp):
        super(OnlyHpHeroFactory, self).__init__()
        self.hp_hero = hp

    def create_hero(self, team_id):
        return BaseHero(self.hp_hero, team_id)
