#! /usr/local/bin/python3
# Caitlin Macleod

"""AoC 2018 Day 3: No Matter How You Slice It

Part one: 

What is the checksum for your list of box IDs?

Part two:

What letters are common between the two correct box IDs?

"""

import collections
import re

claim_re = re.compile(r"#(\d)+ @ (\d+),(\d+): (\d+)x(\d)")

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(parse_claim(line.strip()))
    return input_list

def parse_claim(claim_str):
    """Parse a claim into id, location and size."""
    claim_match = claim_re.match(claim_str)
    claim_dict = {}
    if claim_match is not None:
        claim_dict["id"] = int(claim_match.group(1))
        claim_dict["loc"] = (int(claim_match.group(2)), int(claim_match.group(3)))
        claim_dict["size"] = (int(claim_match.group(4)), int(claim_match.group(5)))
    return claim_dict

def draw_claim(fabric_dict, claim_loc, claim_size):
    """Add 1 to each element in a given rectangle."""
    (cl_x, cl_y) = claim_loc
    (cl_w, cl_t) = claim_size
    for x in range(cl_x, cl_x + cl_w):
        for y in range(cl_y, cl_y + cl_t):
            target = fabric_dict.get((x, y))
            if target is None:
                fabric_dict[(x, y)] = 0
            fabric_dict[(x, y)] += 1

if __name__ == "__main__":
    # Parse inputs
    claims = load_input("d03-input.txt")
    # print(claims)

    # fabric = {collections.defaultdict(lambda: 0)}
    fabric = {}

    for claim in claims:
        draw_claim(fabric, claim["loc"], claim["size"])

    # print(fabric)
    # print(fabric.values())
    num_overlaps = len(list(filter(lambda x: x > 1, fabric.values())))

    print(f"There are {num_overlaps} squares with more than one claim.")
