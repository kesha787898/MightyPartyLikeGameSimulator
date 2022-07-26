from actors.random_actors.RandomActor import RandomActor
from config import hp_first
from factories.first_gen.FirstGenList import all_first_gen
from factories.first_gen.OnlyHpHeroFactory import OnlyHpHeroFactory
from play.Game import AbstractGame
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':

    results = AbstractGame(RandomActor(0, OnlyHpHeroFactory(hp_first), all_first_gen),
                           RandomActor(1, OnlyHpHeroFactory(hp_first), all_first_gen)).play_games(3000)
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
