import os
import string

def get_example_input():
    s = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    return s.splitlines()

def get_input():
    with open('solutions/day12/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def in_grid(self, grid):
        if self.x < 0 or self.y < 0:
            return False
        if self.x >= len(grid[0]):
            return False
        if self.y >= len(grid):
            return False
        return True
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    
    def __str__(self) -> str:
        return f'P({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        return str(self)

def parse_grid(grid):
    parsed = []
    starting_pos = Position(0, 0)
    target = Position(0, 0)
    for y, line in enumerate(grid):
        parsed.append([])
        for x, entry in enumerate(line):
            if entry in string.ascii_lowercase:
                parsed[-1].append(string.ascii_lowercase.index(entry))
            if entry == 'S':
                parsed[-1].append(1)
                starting_pos = Position(x, y)
            if entry == 'E':
                parsed[-1].append(string.ascii_lowercase.index(string.ascii_lowercase[-1]))
                target = Position(x, y)
    return parsed, starting_pos, target

def walk(position, visited, grid, target, length):
    visited.append(position)
    current_height = grid[position.y][position.x]

    if position == target:
        return length

    paths = []
    for direction in [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]:
        new_pos = position + direction
        if new_pos.in_grid(grid) and new_pos not in visited:
            if current_height + 1 >= grid[new_pos.y][new_pos.x]:
                paths.append(walk(position=new_pos, visited=visited, grid=grid, target=target, length=length+1))
    if len(paths) == 0:
        return 999999
    return min(paths)

def task1():
    grid, start, end = parse_grid(get_input())
    return walk(start, [], grid, end, 0) - 2

def task2():
    return ''