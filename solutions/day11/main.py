import os
import re
import operator
from pprint import pprint
import math
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x:x

def get_example_input():
    s = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    return s

def get_input():
    with open('solutions/day11/input.txt') as f:
        return f.read()

PARSE_REGEX = re.compile(r'Monkey (?P<id>\d+):\n\s+Starting items: (?P<items>\d+.*)*\n\s+Operation: new = old (?P<operator>[\+\*-\?]) (?P<rvalue>.*)\n\s+Test: divisible by (?P<test>\d+)\n\s+If true: throw to monkey (?P<truemonkey>\d*)\n\s+If false: throw to monkey (?P<falsemonkey>\d*)')

str_to_op = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv
}

class Monkey:
    def __init__(self, id, items, operation, rvalue, test, true_id, false_id, worry_reduce=True):
        self.id = int(id)
        self.items = [int(x) for x in items.split(', ')]
        self.operation = str_to_op[operation]
        self.rvalue = int(rvalue) if rvalue.isnumeric() else rvalue
        self.test = int(test)
        self.true_id = int(true_id)
        self.false_id = int(false_id)
        self.true_monkey = None
        self.false_monkey = None
        self.times_inspected = 0
        self.worry_reduce = worry_reduce
    
    def ids_to_monkeys(self, table):
        self.true_monkey = table[self.true_id]
        self.false_monkey = table[self.false_id]
    
    def inspect(self, modulo):
        new_item_values = []
        for item in self.items:
            self.times_inspected += 1
            value = 0
            if self.rvalue == 'old':
                value = self.operation(item, item)
            else:
                value = self.operation(item, self.rvalue)
            if self.worry_reduce:
                value = value // 3
            else:
                value = value % modulo
            new_item_values.append(value)
        self.items = new_item_values
    
    def throw(self):
        for item in self.items:
            if item % self.test == 0:
                self.true_monkey.items.append(item)
            else:
                self.false_monkey.items.append(item)
        self.items = []

    def __str__(self):
        return f'Monkey {self.id} with items {self.items}, {self.times_inspected}'
    
    def __repr__(self):
        return str(self)

def run(_input, turns, worry_reduce=True):
    monkeys = []
    table = {}
    for monkey in PARSE_REGEX.finditer(_input):
        monkeys.append(
            Monkey(
                id = monkey['id'],
                items = monkey['items'],
                operation=monkey['operator'],
                rvalue=monkey['rvalue'],
                test=monkey['test'],
                true_id=monkey['truemonkey'],
                false_id=monkey['falsemonkey'],
                worry_reduce=worry_reduce
            )
        )
        table[int(monkey['id'])] = monkeys[-1]
    for monkey in monkeys:
        monkey.ids_to_monkeys(table)
    modulo = 0
    if not worry_reduce:
        modulo = math.prod([monkey.test for monkey in monkeys])
    for t in tqdm(range(turns)):
        for monkey in monkeys:
            monkey.inspect(modulo)
            monkey.throw()
    monkeys_active = sorted(monkeys, key=lambda x: x.times_inspected)
    return monkeys_active[-1].times_inspected * monkeys_active[-2].times_inspected

def task1():
    return run(get_input(), 20, True)

def task2():
    return run(get_input(), 10000, False)