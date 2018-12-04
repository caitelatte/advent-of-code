#!/usr/bin/env python

"""Advent of Code 2017 Day 10 - Knot Hash

http://adventofcode.com/2017/day/10
"""

import operator

LIST_LENGTH = 256 # how many numbers in the orig list.
INPUT_FILENAME = "d10-input.txt"
# INPUT_FILENAME = "d10-input-test-123.txt"

def hash_round(numlist, len_sequence, current_pos, skip_size):
    # do the hash
    for length in len_sequence:
        # print "playing with length {0}".format(length)
        end_index = min(current_pos + length, LIST_LENGTH)
        sel_slice = numlist[current_pos:end_index]
        overflow = max(0, length - len(sel_slice))
        if (overflow > 0):
            # if it needs to wrap around, select remaining from start
            # print "overflow! {0}".format(overflow)
            sel_slice += numlist[:overflow]
        sel_slice.reverse()
        # AW YEAH SLICE ASSIGNMENT
        numlist[current_pos:end_index] = sel_slice[:length-overflow]
        if (overflow > 0):
            # wrap around
            numlist[:overflow] = sel_slice[length-overflow:]
        # print "after slice assignment list of numlist is {0}".format(len(numlist))
        # increment things
        current_pos = (current_pos + length + skip_size) % LIST_LENGTH
        skip_size += 1
    return current_pos, skip_size

if (__name__ == "__main__"):
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        # read in comma-separated line of integers
        raw_line = f.readline()
        num_lengths = map(int, raw_line.strip().split(","))
        byte_lengths = map(ord, raw_line.strip())

    # Part 1 - one round
    numlist = range(0, LIST_LENGTH)
    current_pos = 0
    skip_size = 0
    (current_pos, skip_size) = hash_round(numlist, num_lengths, current_pos, skip_size)
    print numlist
    print numlist[0] * numlist[1]

    # Part 2
    numlist = range(0, LIST_LENGTH)
    current_pos = 0
    skip_size = 0
    for x in range(64):
        (current_pos, skip_size) = hash_round(numlist, byte_lengths, current_pos, skip_size)
    print numlist
    dense = []
    for sixteen in range(LIST_LENGTH/16):
        # print (numlist[(sixteen*16):(sixteen+1)*16])
        dense.append(reduce(
            lambda x, y: x ^ y,
            numlist[(sixteen*16):(sixteen+1)*16]
            ))
    print "DENSE: {0}".format(dense)
    print "HEXKNOT: {0}".format("".join(map(
        lambda x: hex(x)[-2:],
        dense
    )))
