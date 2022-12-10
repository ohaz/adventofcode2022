import os

def get_example_input():
    s = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    return s.splitlines()

def get_input():
    with open('solutions/day10/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def run_noop(context: dict):
    increase_cycle(context=context)

def run_addx(context: dict, amount):
    increase_cycle(context=context)
    increase_cycle(context=context)
    context['x'] += amount

def increase_cycle(context):
    context['cycle'] += 1
    if context['cycle'] in [20, 60, 100, 140, 180, 220]:
        context['signal_strength'] += (context['cycle'] * context['x'])

def task1():
    context = {
        'cycle': 0,
        'x' : 1,
        'signal_strength': 0
    }
    for line in get_input():
        match line.split(' '):
            case ('noop', ):
                run_noop(context)
            case ('addx', amount):
                run_addx(context, int(amount))
                
    return context['signal_strength']

def task2():
    modified_input = []
    for line in get_input():
        match line.split(' '):
            case ('noop', ):
                modified_input.append(('noop'))
            case ('addx', amount):
                modified_input.append(('noop'))
                modified_input.append(('addx', int(amount)))

    crt = [['.' for _ in range(40)] for _ in range(6)]
    crt_index = 0
    x = 1
    x_buffer = 0
    for line in modified_input:
        x += x_buffer
        x_buffer = 0
        match line:
            case ('noop', ):
                pass
            case ('addx', amount):
                x_buffer = amount
        if crt_index % 40 in [x-1, x, x + 1]:
            crt[crt_index // 40][crt_index % 40] = '#'
        crt_index += 1
    result = os.linesep
    for line in crt:
        result += ''.join(line)
        result += os.linesep
    return result