#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 12: Passage Pathing!

Original problem at https://adventofcode.com/2021/day/12
"""

from collections import defaultdict

cave_dict = defaultdict(list)

def find_paths(path_so_far, current_node):
    """"""
    paths = 0
    path_so_far.append(current_node)
    print(f"{path_so_far} -> {cave_dict[current_node]}")

    if current_node == "end":
        # print(f"  end {path_so_far}")
        return 1

    for next_node in cave_dict[current_node]:
        # print(f" {current_node} -> {next_node}")
        # if next_node == "end":
        #     # paths += [path_so_far + [next_node]]
        #     print("  end ", path_so_far)
        #     paths += 1
        if (next_node not in path_so_far or is_big(next_node)):
            paths += find_paths(path_so_far.copy(), next_node)
        
    return paths


def find_paths_p2(path_so_far, current_node, doubled):
    """"""
    paths = 0
    path_so_far.append(current_node)

    if current_node == "end":
        # print(f"{','.join(path_so_far)}")
        return 1
    elif not doubled:
        if path_so_far.count(current_node) > 1 and not is_big(current_node):
            doubled = True
    
    # print(f" {','.join(path_so_far)} -> {cave_dict[current_node]}")

    for next_node in cave_dict[current_node]:
        if next_node != "start":
            if ( is_big(next_node) or (
                path_so_far.count(next_node) == 0
                or not doubled
            )):
                # print(f"  {','.join(path_so_far)} -> {next_node} ({doubled})")
                paths += find_paths_p2(path_so_far.copy(), next_node, doubled)
        
    return paths

def is_big(cave):
    return cave.isupper()

def load_input(input_name):
    """Load the input file (a line-separated list of numbers)."""
    global cave_dict
    with open(input_name) as input_file:
        for connection in input_file:
            (left, right) = connection.strip().split("-")
            cave_dict[left].append(right)
            cave_dict[right].append(left)

if __name__ == "__main__":
    load_input("d12-input.txt")
    print(cave_dict, cave_dict["A"])

    paths = find_paths([], "start")
    print(paths)

    paths = find_paths_p2([], "start", False)
    print(paths)