import os
from collections import defaultdict

def get_example_input():
    s = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    return s.splitlines()

def get_input():
    with open('solutions/day7/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Directory:
    def __init__(self, name, files=None, directories=None, parent=None) -> None:
        self.name = name
        if files is None:
            files = []
        self.files = files
        if directories is None:
            directories = []
        self.directories = directories
        self.parent = parent

    def get_dir_by_name(self, name):
        for child in self.directories:
            if child.name == name:
                return child

    def total_size(self, valid_solutions=None):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.total_size(valid_solutions)
        if size <= 100000 and valid_solutions is not None:
            valid_solutions.append(self)
        return size
    
    def search_fitting_size(self, valid_solutions, searched_size):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.search_fitting_size(valid_solutions, searched_size)
        if size >= searched_size:
            valid_solutions.append(self)
        return size
    
    def to_string(self, depth=0):
        tabs = '\t' * depth
        print(f'{tabs}DIR {self.name}:')
        for child in self.directories + self.files:
            child.to_string(depth=depth+1)

    def __str__(self):
        return f'DIR: {self.name}, {self.total_size()}'
    
    def __repr__(self):
        return str(self)
    
class File:
    def __init__(self, size, name) -> None:
        self.size = int(size)
        self.name = name
    
    def to_string(self, depth=0):
        tabs = '\t' * depth
        print(f'{tabs}FIL {self.name}, {self.size}')

def generate_tree(_input):
    current_directory = None
    root = Directory('/')
    mode = ''
    for line in _input:
        if line.startswith('$'):
            # handle command
            splits = line.split(' ')
            if splits[1] == 'cd':
                if current_directory is None:
                    current_directory = root
                else:
                    if splits[2] == '..':
                        current_directory = current_directory.parent
                    elif splits[2] == '/':
                        current_directory = root
                    else:
                        current_directory = current_directory.get_dir_by_name(splits[2])
            mode = splits[1]
        else:
            if mode == 'ls':
                if line.startswith('dir'):
                    current_directory.directories.append(Directory(line.split(' ')[1], parent=current_directory))
                else:
                    splits = line.split(' ')
                    new_file = File(*splits)
                    current_directory.files.append(new_file)
    return root

def task1():
    root = generate_tree(get_input())
    valid_solutions = []
    root.total_size(valid_solutions=valid_solutions)
    result = 0
    for sol in valid_solutions:
        result += sol.total_size()
    return result

def task2():
    root = generate_tree(get_input())
    free_space = 70000000 - root.total_size()
    free_space_missing = 30000000 - free_space
    valid_solutions = []
    root.search_fitting_size(valid_solutions=valid_solutions, searched_size=free_space_missing)
    solution = min(valid_solutions, key=lambda x: x.total_size())
    return solution.total_size()