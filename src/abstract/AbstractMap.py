from typing import List

from src.abstract.AbstractSquare import AbstractSquare


class AbstractMap:
    def __init__(self):
        pass

    def is_filled(self, x: int, y: int) -> bool:
        raise NotImplementedError()

    def place_unit(self, x: int, y: int):
        raise NotImplementedError()

    def remove_unit(self, x: int, y: int):
        raise NotImplementedError()

    def get_free_squares(self, team_id: int) -> List[AbstractSquare]:
        raise NotImplementedError()

    # Todo not good list[list]
    def get_squares(self) -> List[List[AbstractSquare]]:
        raise NotImplementedError()

    def get_size_x(self) -> int:
        raise NotImplementedError()

    def get_size_y(self) -> int:
        raise NotImplementedError()

    def __str__(self) -> str:
        s = ""
        for y in range(len(self.get_squares()[0])):
            for x in range(len(self.get_squares())):
                s += self[x, y].get_status()[0]
            s += '\n'
        return s

    def __getitem__(self, item):
        if item[1] == -1 and item[0] == -1:
            res = []
            for i in self.get_squares():
                for j in i:
                    res.append(j)
            return res
        if item[1] == -1:
            return self.get_squares()[item[1]]
        if item[0] == -1:
            return [self.get_squares()[item[1]][y] for y in range(len(self.get_squares()))]
        return self.get_squares()[item[0]][item[1]]
