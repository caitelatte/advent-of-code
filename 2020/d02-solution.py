#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 2: Password Philosophy!

Original problem at https://adventofcode.com/2020/day/2

"""
import re

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
    return input_list

def validate_passwd(record):
    """Check if a password is valid by its policy"""
    input_re = r'([0-9]+)-([0-9]+) ([a-z]): (.+)'
    rec_match = re.match(input_re, record.strip())

    (lower, upper, target, passwd) = rec_match.groups()
    return (
        passwd.count(target) >= int(lower)
        and passwd.count(target) <= int(upper))

def better_validate_passwd(record):
    """Check if a password is valid by new policy"""
    input_re = r'([0-9]+)-([0-9]+) ([a-z]): (.+)'
    rec_match = re.match(input_re, record.strip())

    (first, second, target, passwd) = rec_match.groups()

    try:
        first_match = (passwd[int(first) - 1] == target)
    except (IndexError):
        first_match = False
    try:
        second_match = (passwd[int(second) - 1] == target)
    except (IndexError):
        second_match = False
    
    return (
        (first_match and not second_match)
        or (not first_match and second_match)
    )


if __name__ == "__main__":
    records_list = load_input("d02-input.txt")
    valid = 0

    for rec in records_list:
        if validate_passwd(rec):
            valid += 1

    print(f"there were {valid} valid passwords out of {len(records_list)}!")

    q2valid = 0
    for rec in records_list:
        if better_validate_passwd(rec):
            q2valid += 1

    print(f"with the second policy, there were {q2valid} valid passwords!")
