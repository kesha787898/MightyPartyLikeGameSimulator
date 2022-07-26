from typing import List

from src.abstract.AbstractMap import AbstractMap
from src.abstract.AbstractSquare import AbstractSquare
from src.base.MapSquare import MapSquare


# Todo annotate
class BaseMap(AbstractMap):

    def __init__(self, size_x, size_y):
        super().__init__()
        assert size_x % 2 == 0
        self.squares = BaseMap.init_map(size_x, size_y)

    @staticmethod
    def init_map(size_x, size_y):
        res = []
        for x in range(size_x):
            tmp_list = []
            for y in range(size_y):
                tmp_list.append(MapSquare(x, y))
            res.append(tmp_list)
        return res

    def is_filled(self, x: int, y: int):
        return self[x, y].is_filled()

    def place_unit(self, x: int, y: int, ):
        self[x, y].unit_placed()

    def remove_unit(self, x: int, y: int):
        self[x, y].unit_removed()

    def get_free_squares(self, team_id):
        max_x = len(self.squares)
        start_x = 0 if team_id == 0 else max_x // 2
        end_x = max_x // 2 if team_id == 0 else max_x
        res = []
        for pos_x in range(start_x, end_x):
            for pos_y in range(len(self.squares[0])):
                square = self[pos_x, pos_y]
                if not square.is_filled():
                    res.append(self[pos_x, pos_y])
        return res

    def __str__(self):
        s = ""
        for y in range(len(self.squares[0])):
            for x in range(len(self.squares)):
                s += self[x, y].status[0]
            s += '\n'
        return s

    def __getitem__(self, item):
        if item[1] == -1 and item[0] == -1:
            res = []
            for i in self.squares:
                for j in i:
                    res.append(j)
            return res
        if item[1] == -1:
            return self.squares[item[1]]
        if item[0] == -1:
            return [self.squares[item[1]][y] for y in range(len(self.squares))]
        return self.squares[item[0]][item[1]]

    def get_squares(self) -> List[List[AbstractSquare]]:
        return self.squares

    def get_size_x(self) -> int:
        return len(self.get_squares())

    def get_size_y(self) -> int:
        return len(self.get_squares()[0])
