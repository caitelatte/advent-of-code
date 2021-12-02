#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 1: Sonar Sweep

Original problem at https://adventofcode.com/2021/day/1

Input: a list of floor depth readings, from closest to further away.

Output 1: Count of increases between lines.
"""

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(int(line.strip()))
    return input_list

if __name__ == "__main__":
    depths_list = load_input("d01-input.txt")
    current_depth = depths_list[0]
    depth_increases = 0

    for depth in depths_list:
        # print(f"current: {current_depth}, new: {depth}, increase? {depth>current_depth}")
        if (depth > current_depth):
            depth_increases += 1
        current_depth = depth

    print(f"Total depth increases: {depth_increases}")

    current_sum = sum(depths_list[:3])
    sum_increases = 0
    for index in range(len(depths_list)-2):
        new_sum = sum(depths_list[index:index+3])
        # print(f"current: {current_depth}, new: {depth}, increase? {depth>current_depth}")
        if (new_sum > current_sum):
            sum_increases += 1
        current_sum = new_sum
    
    print(f"using sliding sums, the total increases are {sum_increases}")

