from src.abstract.AbstractSquare import AbstractSquare

empty = "EMPTY"
filled = "FILLED"


class MapSquare(AbstractSquare):

    def __init__(self, x: int, y: int):
        super().__init__()
        self.status = empty
        self.x = x
        self.y = y

    def unit_placed(self):
        if self.status == empty:
            self.status = filled
        else:
            raise Exception("place filled")

    def unit_removed(self):
        if self.status == filled:
            self.status = empty
        else:
            raise Exception("place filled")

    def is_filled(self):
        return self.status == filled

    def get_status(self) -> str:
        return self.status

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y
