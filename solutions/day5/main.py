import os
from itertools import zip_longest
import re

def get_example_input():
    s = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    return s.splitlines()

def get_input():
    with open('solutions/day5/input.txt') as f:
        return [x for x in f.readlines()]

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return list(zip_longest(*[iter(iterable)]*n, fillvalue=padvalue))

def parse(line):
    grouped = grouper(4, line, ' ')
    return [x[1] for x in grouped]

def lines_to_stacks(lines):
    stacks = {}
    for index in range(len(lines[0])):
        stacks[index + 1] = []
    for line in lines:
        for index, element in enumerate(line):
            if element != ' ' and not element.isnumeric():
                stacks[index + 1].append(element)
    return stacks

INSTRUCTION_REGEX = re.compile(r'move (?P<amount>\d+) from (?P<start>\d+) to (?P<target>\d+)')

def parse_all(_input):
    instructions = False
    parsed_lines = []
    stacks = None
    parsed_instructions = []
    for line in _input:
        if line.strip() == '':
            instructions = True
            stacks = lines_to_stacks(parsed_lines)
            continue
        if not instructions:
            parsed_lines.append(parse(line))
        if instructions:
            if (m := INSTRUCTION_REGEX.match(line)) is not None:
                parsed_instructions.append([int(m['amount']), int(m['start']), int(m['target'])])
    return parsed_instructions, stacks


def task1():
    parsed_instructions, stacks = parse_all(get_input())

    # amount, start, target
    for instruction in parsed_instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2]].insert(0, stacks[instruction[1]].pop(0))
    
    _max = max(stacks.keys())
    result = ''
    for i in range(1, _max+1):
        if len(stacks[i]) > 0:
            result += stacks[i][0]
    return result

def task2():
    parsed_instructions, stacks = parse_all(get_input())
    # amount, start, target
    for instruction in parsed_instructions:
        to_take = stacks[instruction[1]][:instruction[0]]
        stacks[instruction[2]] = to_take + stacks[instruction[2]]
        stacks[instruction[1]] = stacks[instruction[1]][instruction[0]:]

    _max = max(stacks.keys())
    result = ''
    for i in range(1, _max+1):
        if len(stacks[i]) > 0:
            result += stacks[i][0]
    return result