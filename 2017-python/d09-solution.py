#!/usr/bin/env python

"""Advent of Code 2017 Day 9 - Stream Processing

http://adventofcode.com/2017/day/9

Given a chunk of text which represents a "group", return its total score.

A "group" is consisted of {}
"""

INPUT_FILENAME = "d09-input.txt"

def process_char(char, state):
    """given a character and a state, returns a tuple of result, state

    result may be:
        - "new_group"
        - "end_group"
        - "garbage_char"
        - None

    state may be:
        - "garbage"
        - "garbage_escaped"
        - None
    """
    result = None
    # if escaping a character, nothing matters but changing out of escaped
    if state == "garbage_escaped":
        state = "garbage"
    elif state == "garbage":
        if char == ">":
            state = None
        elif char == "!":
            state = "garbage_escaped"
        else:
            result = "garbage_char"
    elif char == "<":
        state = "garbage"
    elif char == "{":
        result = "new_group"
    elif char == "}":
        result = "end_group"
    elif char != ",":
        print "didn't recognise char " + char
    return result, state

if (__name__ == "__main__"):
    # # Test on simple input
    # in_str = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        in_str = f.read().strip()

    # Process stream
    state = None
    depth = 0
    score = 0
    garbage_chars = 0
    clean_groups = ""
    for char in in_str:
        char_result, state = process_char(char, state)
        if char_result == "new_group":
            depth += 1
            clean_groups += "["
        elif char_result == "end_group":
            score += depth
            clean_groups = clean_groups.strip(",")
            clean_groups += "],"
            depth -= 1
        elif char_result == "garbage_char":
            garbage_chars += 1

    print clean_groups

    print "End depth is " + str(depth)
    print "End score is {0}".format(score)
    print "Number of non-escaped garbage chars is {0}".format(garbage_chars)
