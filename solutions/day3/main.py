import os
import string

CHARACTERS = ' ' + string.ascii_lowercase + string.ascii_uppercase

def get_example_input():
    s = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    return s.splitlines()

def get_input():
    with open('solutions/day3/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def compartments(_input):
    for line in _input:
        yield (line[:len(line)//2], line[len(line)//2:])

def task1():
    points = 0
    for compartment in compartments(get_input()):
        character = set(compartment[0]).intersection(set(compartment[1])).pop()
        points += CHARACTERS.index(character)
    return points

def task2():
    points = 0
    for elf in zip(*[iter(get_input())]*3):
        character = set(elf[0]).intersection(set(elf[1])).intersection(set(elf[2])).pop()
        points += CHARACTERS.index(character)
    return points