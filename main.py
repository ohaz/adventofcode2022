import importlib
import os
import sys

def run(name):
    print(f'----- {name} -----')
    solution = importlib.import_module(f'solutions.{name}.main')
    print(f'Task 1: {solution.task1()}')
    print(f'Task 2: {solution.task2()}')

if __name__ == '__main__':
    to_run = [x for x in os.listdir('solutions') if x.startswith('day')]
    if len(sys.argv) > 1:
        to_run = [f'day{sys.argv[1]}']
    for runnable in to_run:
        run(runnable)