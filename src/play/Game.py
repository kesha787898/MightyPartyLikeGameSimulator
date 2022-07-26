from tqdm import tqdm

from abstract.AbstractActor import AbstractActor
from src.base.BaseEnviroment import BaseEnvironment


class AbstractGame:

    def __init__(self, actor_1: AbstractActor, actor_2: AbstractActor, verbose: int = None):
        self.actors = [actor_1, actor_2]
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


