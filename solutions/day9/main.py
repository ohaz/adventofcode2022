import os
import math

def get_example_input():
    s = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    s = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    return s.splitlines()

def get_input():
    with open('solutions/day9/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def __iadd__(self, other):
        if isinstance(other, Position):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise NotImplementedError('Add not implemented')
    
    def __add__(self, other):
        if not isinstance(other, Position):
            raise NotImplementedError('Add not implemented')
        return Position(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        if not isinstance(other, int):
            raise NotImplementedError('Mul not implemented')
        return Position(self.x * other, self.y * other)
    
    def __sub__(self, other):
        if not isinstance(other, Position):
            raise NotImplementedError('Sub not implemented')
        return Position(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f'(x={self.x}, y={self.y})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        _hash = 900000 + self.x * 1000 + self.y
        return _hash

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Position):
            raise NotImplementedError()
        return self.x == __o.x and self.y == __o.y

vectors = {
    'R': Position(1, 0),
    'L': Position(-1, 0),
    'U': Position(0, 1),
    'D': Position(0, -1)
}

def get_closer(_head, _pos):
    difference = _head - _pos
    return _pos + Position(
        0 if difference.x == 0 else int(math.copysign(1, difference.x)),
        0 if difference.y == 0 else int(math.copysign(1, difference.y)),
    )

def task1():
    head = Position()
    tail = Position()
    visited = set()
    visited.add(tail)

    for line in get_input():
        direction, amount = line.split(' ')
        head += (vectors[direction] * int(amount))
        difference = head - tail
        if difference.length() >= 2:
            _pos = tail
            while difference.length() > 1:
                _pos = get_closer(head, _pos)
                visited.add(_pos)
                difference = head - _pos
            tail = _pos
    return len(visited)

def task2():
    head = Position()
    tails = [Position() for _ in range(9)]
    visited = set()
    visited.add(Position())

    for line in get_input():
        direction, amount = line.split(' ')
        for _ in range(int(amount)):
            head += vectors[direction]
            for previous, knot in zip([head] + tails, tails):
                difference = previous - knot
                if difference.length() >= 2:
                    _pos = Position(knot.x, knot.y)
                    while difference.length() >= 2:
                        _pos = get_closer(previous, _pos)
                        if knot is tails[-1]:
                            visited.add(Position(_pos.x, _pos.y))
                        difference = previous - _pos
                    knot.x = _pos.x
                    knot.y = _pos.y
    return len(visited)