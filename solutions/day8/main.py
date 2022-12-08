import os
from pprint import pprint
import operator

def get_example_input():
    s = """30373
25512
65332
33549
35390"""
    return s.splitlines()

def get_input():
    with open('solutions/day8/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class GridEntry:
    def __init__(self, value, visible=False):
        self.value = int(value)
        self.visible = visible
    
    def __str__(self):
        return f'({self.value}, {self.visible})'
    
    def __repr__(self) -> str:
        return str(self)

def task1():
    grid = []
    for line in get_input():
        l = [GridEntry(x) for x in line]
        grid.append(l)
    
    # Make borders visible
    for i in range(len(grid)):
        grid[i][0].visible = True
        grid[i][len(grid[i])-1].visible = True
    for i in range(len(grid[0])):
        grid[0][i].visible = True
        grid[len(grid)-1][i].visible = True
    # Shooting sun rays 
    
    ## Up and down
    ray_vector = (1, 0)
    ray_position = (0, 0)
    max_found = 0
    for start_position in range(len(grid[0])):
        while ray_position[0] < len(grid):
            entry = grid[ray_position[0]][ray_position[1] + start_position]
            value = entry.value
            if value > max_found:
                max_found = value
                entry.visible = True
            ray_position = tuple(map(operator.add, ray_position, ray_vector))
        max_found = 0
        ray_position = (0, 0)
    ray_vector = (-1, 0)
    ray_position = (len(grid)-1, 0)
    max_found = 0
    for start_position in range(len(grid[0])):
        while ray_position[0] >= 0:
            entry = grid[ray_position[0]][ray_position[1] + start_position]
            value = entry.value
            if value > max_found:
                max_found = value
                entry.visible = True
            ray_position = tuple(map(operator.add, ray_position, ray_vector))
        max_found = 0
        ray_position = (len(grid)-1, 0)
    ## Left and Right
    ray_vector = (0, 1)
    ray_position = (0, 0)
    max_found = 0
    for start_position in range(len(grid)):
        while ray_position[1] < len(grid[0]):
            entry = grid[ray_position[0] + start_position][ray_position[1]]
            value = entry.value
            if value > max_found:
                max_found = value
                entry.visible = True
            ray_position = tuple(map(operator.add, ray_position, ray_vector))
        max_found = 0
        ray_position = (0, 0)
    ray_vector = (0, -1)
    ray_position = (0, len(grid[0])-1)
    max_found = 0
    for start_position in range(len(grid)):
        while ray_position[1] >= 0:
            entry = grid[ray_position[0] + start_position][ray_position[1]]
            value = entry.value
            if value > max_found:
                max_found = value
                entry.visible = True
            ray_position = tuple(map(operator.add, ray_position, ray_vector))
        max_found = 0
        ray_position = (0, len(grid[0])-1)
    
    amount = 0
    for row in grid:
        for element in row:
            if element.visible:
                amount += 1
    return amount

def task2():
    grid = []
    for line in get_input():
        l = [GridEntry(x) for x in line]
        grid.append(l)
    value = 0 
    for row_index, row in enumerate(grid):
        for column_index, entry in enumerate(row):
            if row_index == 3 and column_index == 2:
                pass
            if row_index == 1 and column_index == 4:
                pass
            # left
            left_count = 0
            for i in reversed(range(0, column_index)):
                left_count += 1
                if grid[row_index][i].value >= entry.value:
                    break
            # right
            right_count = 0
            for i in range(column_index + 1, len(grid[0])):
                right_count += 1
                if grid[row_index][i].value >= entry.value:
                    break
            # up
            up_count = 0
            for i in reversed(range(0, row_index)):
                up_count += 1
                if grid[i][column_index].value >= entry.value:
                    break
            # bottom
            down_count = 0
            for i in range(row_index + 1, len(grid)):
                down_count += 1
                if grid[i][column_index].value >= entry.value:
                    break
            value = max(value, left_count * right_count * up_count * down_count)
    return value