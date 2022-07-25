from src.abstract.RenameMe import AliveObject, WithId


class AbstractHero(AliveObject, WithId):
    def __init__(self, hp: int):
        super().__init__(hp)
