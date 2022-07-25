from abstract.AbstractEnviroment import AbstractEnvironment


class AbstractActor:
    def place_hero(self, env: AbstractEnvironment):
        raise NotImplementedError()

    def place_unit(self, env: AbstractEnvironment):
        raise NotImplementedError()

    def attack(self, env: AbstractEnvironment):
        raise NotImplementedError()
