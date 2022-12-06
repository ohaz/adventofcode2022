import os

def get_example_input():
    s = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
    return s

def get_input():
    with open('solutions/day6/input.txt') as f:
        return f.read().strip()

def search_marker(text, length):
    for i in range(len(text) - length - 1):
        if length == len(set([*text[i:i+length]])):
            return i+length

def task1():
    _input = get_input()
    return search_marker(_input, 4)

def task2():
    _input = get_input()
    return search_marker(_input, 14)