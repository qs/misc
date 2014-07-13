#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint, choice


class AbstractBattleSkill:
    def __init__(self, name, ap):
        self.name = name
        self.ap = ap

    def use(self, author, aim=None):
        raise Exception('must be overloaded in subclasses')

    @classmethod
    def get_battle_skills(cls):
        return cls.__subclasses__


class BattleSkillBeat(AbstractBattleSkill):
    def use(self, author, aim):
        aim.get_dmg(author)


class BattleAction:
    def __init__(self, author, skill, aim=None):
        self.author = author
        self.skill = skill
        self.aim = aim
        self.ap = skill.ap

    def do(self):
        skill.use(self.author, self.aim)


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
        if 'ap' not in kwargs:
            kwargs['ap'] = randint(8,10)
        self.name = self._gen_name()
        self.score = self.compute_score()
        
        self.battle_status = True  # alive
        self.battle_auras = []
        self.battle_skills = []
        self.battle_actions = []

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
        return self.hp + self.dmg * 5 + self.spd + self.ap * 8

    def choose_strategy(self):
        # fill battle_actions
        pass

    def turn(self):
        # do battle_actions
        for action in self.battle_actions:
            action.do()


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
        self.characters_alive = self.characters
        self.turn = 0
        self.status = 0  # 0 - in progress, 1 - finished

    def compute_turn(self):
        # testing random
        for ch in self.characters:
            ch.battle_actions = []
            ch.battle_skills = list(set([choice(AbstractBattleSkill.get_battle_skills()) for i in range(4)]))

        # turning
        while self.status == 0:
            for ch in self.characters:
                ch.choose_strategy()

            for ch in self.characters_alive:
                ch.turn()
                self.remove_dead()
                self.check_victory()
            self.turn += 1

    def remove_dead(self):
        for ch in self.characters_alive:
            if ch.hp <= 0:
                self.characters_alive.remove(ch)

    def check_victory(self):
        # TODO refactor
        sides_alive = []
        for side in self.sides:
            if set(self.characters_alive) & set(side.characters):
                sides_alive.append(side)
        if len(set(sides_alive)) == 1:
            print 'End of battle'
            self.status = 1

# characters generating
chars_lst = []
for i in range(10):
    chars_lst.append(Character())

# sides generating
sides_num = 3
chars_lst = sorted(chars_lst, reverse=True, key=lambda x: x.score)
sides = [Side([]) for i in range(sides_num)]

for ch in chars_lst:
    weakest_side = min(sides, key=lambda x: x.score)
    weakest_side.add_character(ch)

print sides

# battle begin
battle = Battle(sides)