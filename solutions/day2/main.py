import os
from enum import Enum
from itertools import cycle

def get_example_input():
    s = """A Y
B X
C Z"""
    return s.splitlines()

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

translation_table = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

translation_table_rps = {
    'A': RPS.ROCK,
    'B': RPS.PAPER,
    'C': RPS.SCISSORS,
}

victories = {
    RPS.ROCK: RPS.SCISSORS,
    RPS.PAPER: RPS.ROCK,
    RPS.SCISSORS: RPS.PAPER,
}

need_to = { # second character input and enemy value input
    'X': { # loose
        RPS.ROCK: RPS.SCISSORS,
        RPS.PAPER: RPS.ROCK,
        RPS.SCISSORS: RPS.PAPER,
    },
    'Y': { # draw
        RPS.ROCK: RPS.ROCK,
        RPS.PAPER: RPS.PAPER,
        RPS.SCISSORS: RPS.SCISSORS,
    },
    'Z': { # win
        RPS.ROCK: RPS.PAPER,
        RPS.PAPER: RPS.SCISSORS,
        RPS.SCISSORS: RPS.ROCK,
    }
}

def outcome(me, other):
    '''
    Returns 0 on loss, 1 on draw, 2 on win
    '''
    if me == other:
        return 1
    if victories[me] == other:
        return 2
    return 0


def outcome_score(me, other):
    return outcome(me, other) * 3

def get_input():
    with open('solutions/day2/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    result = 0
    for line in get_input():
        enemy, me = line.split(' ')
        enemy = translation_table_rps[enemy]
        me = translation_table_rps[translation_table[me]]
        result += outcome_score(me, enemy) + me.value
    return result

def task2():
    result = 0
    for line in get_input():
        enemy, me = line.split(' ')
        need_to_table = need_to[me]
        enemy = translation_table_rps[enemy]
        me = need_to_table[enemy]
        result += outcome_score(me, enemy) + me.value
    return result