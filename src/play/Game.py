import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

from src.base.BaseEnviroment import BaseEnvironment
from src.actors.random_actors.RandomActor import RandomActor
from src.config import hp_second, hp_first
from src.factories.first_gen.FirstGenList import all_first_gen
from src.factories.first_gen.OnlyHpHeroFactory import OnlyHpHeroFactory


class AbstractGame:

    def __init__(self, verbose=None):
        self.actors = [RandomActor(0, OnlyHpHeroFactory(hp_first), all_first_gen),
                       RandomActor(1, OnlyHpHeroFactory(hp_second), all_first_gen)]
        self.verbose = verbose

    def play_game(self):
        env = BaseEnvironment()
        if self.verbose:
            print(env)
        for actor in self.actors:
            actor.place_hero(env)
        while True:
            for actor in self.actors:
                actor.place_unit(env)
                actor.attack(env)
                status = env.get_status()
                if status == "finished":
                    if self.verbose:
                        print(env)
                    return env.winner, env.heroes[0].hp, env.heroes[1].hp
            if self.verbose:
                print(env)

    def play_games(self, num):
        game_results = []
        for _ in tqdm(range(num)):
            result = self.play_game()
            game_results.append(result)
        return game_results


if __name__ == '__main__':

    results = AbstractGame().play_games(3000)
    winners = []
    hps0 = []
    hps1 = []
    for winner, hp0, hp1 in results:
        winners.append(winner)
        hps0.append(hp0)
        hps1.append(hp1)
    print(sum(winners) / len(winners))
    print(sum(hps0) / len(hps0))
    print(sum(hps1) / len(hps1))

    plt.plot([sum(winners[:i]) / len(winners[:i]) for i in range(1, len(winners))])
    plt.show()
    sns.distplot([j - i for i, j in zip(hps0, hps1)])
    plt.show()
