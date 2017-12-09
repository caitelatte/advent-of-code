#!/usr/bin/env python

"""Advent of Code 2017 Day 1 - captcha

input: file with string of integers (one line)

output: integer - sum of each digit which is the same as the next digit in
    the list. The last digit should be included if it's the same as the first.
"""

INPUT_FILENAME = "d01-input.txt"

def sumMatchingNums(inputlist):
    """Find the sum of the numbers in a list which match the next."""
    return sum(findMatchingNums(inputlist))

def findMatchingNums(inputlist):
    """Filter a list of integers to just ones that match the next.

    The last digit may match the first digit.
    """
    outlist = []
    for i in range(len(inputlist)):
        if (i+1 in range(len(inputlist))):
            if (inputlist[i] == inputlist[i+1]):
                outlist.append(inputlist[i])
        else:
            # Last digit matches first
            if (inputlist[i] == inputlist[0]):
                outlist.append(inputlist[i])
    # print "matching numbers: {0}".format(outlist)
    return outlist

if (__name__ == "__main__"):
    # Set up array full of ints
    with (open(INPUT_FILENAME)) as f:
        numstring = f.readline().strip()
        try:
            numlist = map(lambda x: int(x), numstring)
        except ValueError as e:
            print "There's something in that file I don't like!"
            raise
    # print "all numbers: {0}".format(numlist)

    # Sum numlist according to weird christmas rules
    numsum = sumMatchingNums(numlist)
    print "Wow! I applied some weird christmas logic to that list and came up with this number: {0}".format(
        numsum
    )
