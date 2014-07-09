class Character:
    def __init__(self, **kwargs):
        for k, v in kwargs:
             setattr(self, k, v)


class Side:
    def __init__(self, characters, color=None):
        self.characters = characters


class Battle:
    def __init__(self, sides):
        self.sides = sides  # lists of Sides
        self.characters = sorted([i for j in sides for i in j.characters], key=lambda x: x.speed)
        self.turn = 0

    def compute_turn(self):
        for ch in self.characters:
            ch.choose_strategy()

        for ch in self.characters:
            ch.turn()