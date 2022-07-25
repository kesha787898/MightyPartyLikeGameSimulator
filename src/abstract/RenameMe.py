class MapObject:
    def __init__(self):
        self.x = -1
        self.y = -1

    def on_placed(self, x: int, y: int):
        self.x = x
        self.y = y


class AliveObject:
    def __init__(self, hp: int):
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def on_attacked(self, unit):
        damage = unit.base_attack_power
        self.hp -= damage


class WithId:
    counter = 0

    def __init__(self):
        self.id = WithId.counter
        WithId.counter += 1
