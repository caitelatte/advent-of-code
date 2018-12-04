#!/usr/bin/env python

"""Advent of Code 2017 Day 07 - Recursive Circus

http://adventofcode.com/2017/day/7

Find the root node name of a tree of "programs".

Given: list of nodes, weight and names of child nodes
in format "xxxx (ww) -> yyyy, zzzz"
"""

import re

INPUT_FILENAME = "d07-input.txt"
RE_NODE = r"^([a-z]+) \(([0-9]+)\)"
RE_PARENT_NODE = RE_NODE + r" -> ((?:[a-z]+(?:, )?)+)$"
end_node_re = re.compile(RE_NODE)
parent_node_re = re.compile(RE_PARENT_NODE)

def parse_node(line, tree_weights, tree_children):
    line_node_match = end_node_re.match(line)
    if line_node_match is not None:
        node_name = line_node_match.group(1)
        tree_weights[node_name] = int(line_node_match.group(2))
        # Check if children
        line_parent_match = parent_node_re.match(line)
        if line_parent_match is not None:
            tree_children[node_name] = line_parent_match.group(3).split(", ")
    else:
        print "WARN: Couldn't match line {0}".format(line)

if (__name__ == "__main__"):
    tree_weights = {}
    tree_children = {}
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        for line in f:
            parse_node(line, tree_weights, tree_children)
    print tree_children
