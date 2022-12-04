import os
import re

def get_example_input():
    s = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    return s.splitlines()

def get_input():
    with open('solutions/day4/input.txt') as f:
        return [x.strip() for x in f.readlines()]

PARSE_PATTERN = re.compile(r'(?P<start1>\d+)-(?P<end1>\d+),(?P<start2>\d+)-(?P<end2>\d+)')

def task1():
    counter = 0
    for line in get_input():
        if (m := PARSE_PATTERN.match(line)) is not None:
            start1, start2, end1, end2 = int(m['start1']), int(m['start2']), int(m['end1']), int(m['end2'])
            if (start1 in range(start2, end2+1) and end1 in range(start2, end2+1)) or \
                (start2 in range(start1, end1+1) and end2 in range(start1, end1+1)):
                counter += 1
    return counter

def task2():
    counter = 0
    for line in get_input():
        if (m := PARSE_PATTERN.match(line)) is not None:
            start1, start2, end1, end2 = int(m['start1']), int(m['start2']), int(m['end1']), int(m['end2'])
            if (start2 in range(start1, end1+1)) or (start1 in range(start2, end2+1)):
                counter += 1
    return counter