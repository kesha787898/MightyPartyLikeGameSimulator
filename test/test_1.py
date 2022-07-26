from actors.random_actors.RandomActor import RandomActor
from config import hp_first
from factories.first_gen.FirstGenList import all_first_gen
from factories.first_gen.OnlyHpHeroFactory import OnlyHpHeroFactory
from src.play.Game import AbstractGame


def test_game():
    AbstractGame(RandomActor(0, OnlyHpHeroFactory(hp_first), all_first_gen),
                 RandomActor(1, OnlyHpHeroFactory(hp_first), all_first_gen)
                 ).play_games(3000)
