#!/usr/bin/env python

"""Advent of Code 2017 Day 6 - Memory Reallocation

http://adventofcode.com/2017/day/6

There are 16 memory banks, which can hold any number of blocks.

Reallocation wants to balance blocks between banks.

Per cycle:
    - find memory bank with most blocks
        - ties won by lowest-numbered bank
    - redistributes those blocks among banks
        - remove all from that bank
        - deposit those blocks in the other banks one by one

How many redistributions can be done before a config is produced that has been seen before?
"""

INPUT_FILENAME = "d06-input.txt"

def distribute_blocks(banks):
    num_blocks = max(banks)
    current_bank = banks.index(num_blocks) #selects the first if tied
    banks[current_bank] = 0
    while (num_blocks > 0):
        current_bank = (current_bank + 1) % len(banks) #wrap around
        banks[current_bank] += 1
        num_blocks -= 1

if (__name__ == "__main__"):
    states = set()
    iterations = 0
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        banks = map(int, f.readline().split())
    print "Initial banks setup: {0}".format(banks)
    while str(banks) not in states:
        states.add(str(banks))
        iterations += 1
        distribute_blocks(banks)
    print "It took {0} iterations to reach a repeat state!".format(iterations)
    # See how long until it comes back to the same?
    states = set()
    iterations = 0
    while str(banks) not in states:
        states.add(str(banks))
        iterations += 1
        distribute_blocks(banks)
    print "It took {0} iterations to reach a repeat state for the second time!".format(iterations)
