#!/usr/bin/env python

"""Advent of Code 2017 Day 1 - captcha

http://adventofcode.com/2017/day/1

input: file with string of integers (one line)

output part 1: integer - sum of each digit which is the same as the next digit
    in the list. The last digit should be included if it's the same as the
    first.
output part 2: consider the digit halfway around the circular list.
"""

INPUT_FILENAME = "d01-input.txt"

def sumNextMatchingNums(inputlist):
    """Find the sum of the numbers in a list which match the next."""
    return sum(findNextMatchingNums(inputlist))

def findNextMatchingNums(inputlist):
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

def sumOppMatchingNums(inputlist):
    """Find the sum of the numbers in a list which match the next."""
    return sum(findOppMatchingNums(inputlist))

def findOppMatchingNums(inputlist):
    """Filter a list of integers to just ones that match their opposite.

    The "opposite" number is the number which is halfway along the list.
    """
    outlist = []
    try:
        length = len(inputlist)
        half = int(length/2)
    except ValueError as e:
        print "No fair! The computer said the input list length would be even , but it was {0} elements long instead!".format(len(inputlist))
        raise
    for i in range(length):
        oppindex = (i + half) % length # wrap numbers back around if larger than the list
        if (inputlist[i] == inputlist[oppindex]):
            outlist.append(inputlist[i])
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
    nextsum = sumNextMatchingNums(numlist)
    print "Wow! I applied some weird christmas logic to that list and came up with this number: {0}".format(
        nextsum
    )
    halfwaysum = sumOppMatchingNums(numlist)
    print "And if you were wondering what would happen if you checked if the opposite number matched, here you are: {0}".format(
        halfwaysum
    )
