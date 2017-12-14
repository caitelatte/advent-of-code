#!/usr/bin/env python

"""Advent of Code 2017 Day 3 - Spiral Memory

Memory is stored on an infinite two-dimensional grid, spiraling out from a central point "1".

Input: a location on that grid
Output 1: How many steps it must be carried (in manhattan distance) to reach spot 1.
"""

import math

INPUT = 325489

def spiralDepth(num):
    """Return the layer of a spiral that this number is in.

    The last number in each layer is x ** 2 where x is an odd number (eg 9, 25, 49, 81)."""
    
    return result

def spiralQuadrant(num):
    """Return the quadrant of a spiral layer of a number."""
    depth = spiralDepth(num)
    beginning = depth ** 2
    end = ((depth+1) ** 2) - 1


if (__name__ == "__main__"):
    print "The given number is in layer {0}".format(
        spiralDepth(INPUT)
    )
