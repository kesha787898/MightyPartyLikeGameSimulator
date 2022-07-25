class AbstractSquare:
    def __init__(self):
        pass

    def unit_placed(self):
        raise NotImplementedError()

    def unit_removed(self):
        raise NotImplementedError()

    def is_filled(self) -> bool:
        raise NotImplementedError()

    def get_status(self) -> str:
        raise NotImplementedError()

    def get_x(self) -> int:
        raise NotImplementedError()

    def get_y(self) -> int:
        raise NotImplementedError()
