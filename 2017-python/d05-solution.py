#!/usr/bin/env python

"""Advent of Code 2017 Day 5 - A Maze of Twisty Trampolines, All Alike

http://adventofcode.com/2017/day/5
"""

INPUT_FILENAME = "d05-input.txt"

instructions = []

def follow_instruction(index):
    result = index + instructions[index]
    instructions[index] += 1
    return result

def follow_weirder_instructions(index):
    result = index + instructions[index]
    if (instructions[index] >= 3):
        instructions[index] -= 1
    else:
        instructions[index] += 1
    return result

if (__name__ == "__main__"):
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        for line in f:
            instructions.append(int(line.strip()))
    instructions_length = len(instructions)
    original_instructions = instructions[:]
    # Follow instructions until out of the list
    current_index = 0
    steps = 0
    while ((current_index >= 0) and (current_index < instructions_length)):
        current_index = follow_instruction(current_index)
        steps += 1
    print "I got out!! In {0} steps.".format(steps)
    # Follow weirder instructions until out of the list
    instructions = original_instructions[:]
    current_index = 0
    steps = 0
    while ((current_index >= 0) and (current_index < instructions_length)):
        current_index =  follow_weirder_instructions(current_index)
        steps += 1
    print "I got out even with weirder instructions!! In {0} steps.".format(steps)
