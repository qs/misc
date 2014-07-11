from random import randint, choice

class Character:
    def __init__(self, **kwargs):
        if 'dmg' not in kwargs:
            kwargs['dmg'] = randint(3, 7)
        if 'hp' not in kwargs:
            kwargs['hp'] = randint(60, 120)
        if 'hp_max' not in kwargs:
            kwargs['hp_max'] = kwargs['hp']
        if 'spd' not in kwargs:
            kwargs['spd'] = randint(1,5)
        self.name = self._gen_name()
        for k, v in kwargs.items():
             setattr(self, k, v)
        self.score = self.compute_score()

    def __repr__(self):
        return '<Char:%s hp:%s/%s dmg:%s spd:%s score:%s>' % \
                (self.name, self.hp, self.hp_max, self.dmg, self.spd, self.score)

    def _gen_name(self):
        s = 'qrtpsdfghjklzxcvbnm'
        g = 'euioa'
        name = ''.join([choice(s) if ltr == 's' else choice(g) \
                for tpl in choice(['ssgsg', 'gsgss', 'sgsgs', 'sggssg']) for ltr in tpl])
        return name.title()

    def compute_score(self):
        return self.hp + self.dmg * 5 + self.spd

    def choose_strategy(self):
        pass

    def turn(self):
        pass


class Side:
    def __init__(self, characters, color=None):
        self.characters = characters
        self.score = sum([ch.score for ch in characters])

    def add_character(self, character):
        self.characters.append(character)
        self.score += character.score

    def __repr__(self):
        return '<Side: score:%s chars:%s>' % (self.score, len(self.characters))


class Battle:
    def __init__(self, sides):
        self.sides = sides  # lists of Sides
        self.characters = sorted([i for j in sides for i in j.characters], key=lambda x: x.spd)
        self.turn = 0

    def compute_turn(self):
        for ch in self.characters:
            ch.choose_strategy()

        for ch in self.characters:
            ch.turn()


chars_lst = []
for i in range(4):
    chars_lst.append(Character())

chars_lst = sorted(chars_lst, reverse=True, key=lambda x: x.score)

sides_num = 3
sides = [Side([]) for i in range(sides_num)]

for ch in chars_lst:
    weakest_side = min(sides, key=lambda x: x.score)
    weakest_side.add_character(ch)

print sides

battle = Battle(sides)