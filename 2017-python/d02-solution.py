#!/usr/bin/env python

"""Advent of Code 2017 Day 2 - Corruption Checksum

input: tab-seperated file of numbers

Given a spreadsheet, for each row determine the difference between the largest and smallest values. Return the sum of all of these values.
"""

INPUT_FILENAME = "d02-input.txt"

def rowDiff(row):
    """Return the difference between the max and min values in a list"""
    return (max(row) - min(row))

def rowDivisible(row):
    """Return result of division of the only two evenly divisible numbers in a list"""
    result = None
    for i in range(len(row)):
        matches = filter(lambda y: (row[i] / float(y)) % 1 == 0, row) # filter to only things which divide evenly with the selected thing
        if len(matches) > 1:
            # Is it dividing evenly with more than itself?
            # print "found some matches with {0}! {1}".format(row[i], matches)
            if matches[0] != row[i]:
                # Is the first item different to the original one?
                result = row[i] / matches[0]
            else:
                # They might both be the same as the original, don't check.
                result = row[i] / matches[1]
    return result

if (__name__ == "__main__"):
    # Take in input from file
    rows = []
    with (open(INPUT_FILENAME)) as f:
        for line in f:
            try:
                rows.append(map(int, line.split()))
            except ValueError as e:
                print "rude, the spreadsheet couldn't be split and parsed as integers."
                raise
    # Calculate the checksum
    checksum = sum(map(rowDiff, rows))
    print "The checksum of the spreadsheet is {0}".format(checksum)
    # Calculate the evenly divisible sum thing
    evenlydivisiblesumthing = sum(map(rowDivisible, rows))
    print "The Evenly Divisible Sum Thing is {0}".format(evenlydivisiblesumthing)
