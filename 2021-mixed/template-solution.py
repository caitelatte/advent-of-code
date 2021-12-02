#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 1: Dive!

Original problem at https://adventofcode.com/2021/day/2

"""

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
    return input_list

if __name__ == "__main__":
    depths_list = load_input("d01-input.txt")