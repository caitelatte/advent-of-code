#!/usr/bin/env python

"""Advent of Code 2017 Day 9 - Stream Processing

http://adventofcode.com/2017/day/9

Given a chunk of text which represents a "group", return its total score.

== Input ==

Section of text which contains "groups" of comma-separated  nested "groups" or
garbage sections.

Groups are defined by a "{" followed by a "}".

Garbage sections begin with a "<" and end with a ">" and may contain arbitrary
text. Inside garbage sections, any character following a "!" is to be ignored,
including a ">".

There are no characters outside of the set ("{", "}", ",", "<", ">") outside of
garbage sections.

== Output 1 ==

The "score" of the section. This is calculated by summing the depth of each
group.

== Output 2 ==

The number of non-escaped characters included within garbage sections in the
input text.

== Solution ==

I made a flexible function (process_char) to parse each character given a
pre-existing state, and return both a new state and any important information
about that character (eg that it's begun or ended a new group).

I carefully ordered the ifs and elifs in this function to match the order in
which characters and states need to be processed. e.g. if in escaped mode,
don't process any characters and change state right away

First I was most concerned about correctly parsing the characters. I caught
the "new_group" and "end_group" events from the process_char() function and
added a "[" or "]," to a string so that I could copy it into python and check
if I'd parsed a correct nested list structure. I also kept track of how deeply
nested I was so that I could easily tell if there were unmatched brackets.

Initially this failed pretty badly (the depth variable was at -391). I'd tried
to affect the "state" variable passed into process_char from within the
function but that didn't work how I expected. To work around that problem I
changed process_char to return a tuple of result and state, and reassigned
the main variable of state each function call in the external loop.

Then it worked! and everything was good

For the second part I needed to track the non-escaped characters within garbage
sections, which I could easily do with an else statement inside process_char,
a new result type and the matching statement in the external loop section.
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

    print "If you want to put the parsed result into a python parser, here it is:\n{0}".format(clean_groups)

    print "End score is {0}".format(score)
    print "Number of non-escaped garbage chars is {0}".format(garbage_chars)
