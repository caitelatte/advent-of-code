#!/usr/bin/env python

"""Advent of Code 2017 Day 8 - I Heard You Like Registers

http://adventofcode.com/2017/day/8

Given a set of instructions to conditionally increment or decrement registers, return the largest value in any register after following each.
"""

INPUT_FILENAME = "d08-input.txt"

def parse_instruction(instruct):
    """Given a line of instruction, return a dictionary of how to use it.
    """
    spl_instruct = instruct.split()
    if spl_instruct[1] == "inc":
        increment = int(spl_instruct[2])
    else:
        increment = -int(spl_instruct[2])
    return {
        "target_name": spl_instruct[0],
        "target_inc": increment,
        "cond_name": spl_instruct[4],
        "cond_bool": spl_instruct[5],
        "cond_val": int(spl_instruct[6])
    }


def process_instruction(instruct, registers):
    """Given an instruction and a set of registers, update the register."""
    global max_val
    p_ins = parse_instruction(instruct)
    # calculate the conditional
    cond_true = False
    cond_reg = registers.get(p_ins["cond_name"], 0)
    if p_ins["cond_bool"] == "==":
        cond_true = (cond_reg == p_ins["cond_val"])
    elif p_ins["cond_bool"] == "!=":
        cond_true = (cond_reg != p_ins["cond_val"])
    elif p_ins["cond_bool"] == ">":
        cond_true = (cond_reg > p_ins["cond_val"])
    elif p_ins["cond_bool"] == ">=":
        cond_true = (cond_reg >= p_ins["cond_val"])
    elif p_ins["cond_bool"] == "<":
        cond_true = (cond_reg < p_ins["cond_val"])
    elif p_ins["cond_bool"] == "<=":
        cond_true = (cond_reg <= p_ins["cond_val"])

    if cond_true:
        # update register if conditional true
        new_val = registers.get(p_ins["target_name"], 0) + p_ins["target_inc"]
        registers[p_ins["target_name"]] = new_val
        if new_val > max_val:
            max_val = new_val
        print "{result}: ({comp_name}) {comp_value} {cond_bool} {cond_val}, therefore incrementing {target_name} by {target_inc}".format(
            result=cond_true,
            comp_name=p_ins["cond_name"],
            comp_value=cond_reg,
            cond_bool=p_ins["cond_bool"],
            cond_val=p_ins["cond_val"],
            target_name=p_ins["target_name"],
            target_inc=p_ins["target_inc"]
        )


if (__name__ == "__main__"):
    instructions = []
    registers = {}
    global max_val
    max_val = 0
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        for line in f:
            process_instruction(line.strip(), registers)

    print "The largest value is: " + str(max(registers.values()))

    print "The largest value at any time during the calculation was: " + str(max_val)
