import os

def get_example_input():
    s = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    return s.splitlines()

def get_input():
    with open('solutions/day1/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def calculate_sums(lines):
    sums = [0]
    for line in lines:
        if line == '':
            sums.append(0)
            continue
        sums[-1] += int(line)
    return sorted(sums)

def task1():
    return sum(calculate_sums(get_input())[-1:])

def task2():
    return sum(calculate_sums(get_input())[-3:])