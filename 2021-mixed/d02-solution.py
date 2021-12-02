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

def simple_process_input(directions):
    """Adjust depth or horiz based on input directions"""
    horiz = 0
    depth = 0

    for line in directions:
        (change, distance) = line.split(" ")
        if (change == "forward"):
            horiz += int(distance)
        elif (change == "down"):
            depth += int(distance)
        elif (change == "up"):
            depth -= int(distance)
    return (horiz, depth)

def process_aim(direction):
    """Adjust horiz, depth and aim based on directions"""
    hor = 0
    dep = 0
    aim = 0

    for line in directions:
        (change, distance) = line.split(" ")
        if (change == "forward"):
            hor += int(distance)
            dep += aim * int(distance)
        elif (change == "down"):
            aim += int(distance)
        elif (change == "up"):
            aim -= int(distance)
    
    return (hor, dep)


if __name__ == "__main__":
    directions = load_input("d02-input.txt")

    (horiz, depth) = simple_process_input(directions)

    print(f"The \"final\" horizontal position is {horiz} and depth is {depth}")
    print(f"With their powers combined, they make {depth*horiz}")

    (hor, dep) = process_aim(directions)

    print(f"The *final* horizontal position is {hor} and depth is {dep}")
    print(f"With their powers combined, they make {hor*dep}")

