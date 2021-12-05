#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 3: Binary Diagnostic

Original problem at https://adventofcode.com/2021/day/3
"""
from functools import partial

column_length = 0
binary_cols = []

def filter_oxygen(binary_lines, col=0):
    """Determine most common value in current column"""
    if len(binary_lines) == 1:
        return binary_lines[0]
    current_column = list(map(lambda x: x[col], binary_lines))
    # print(current_column)
    one_count = current_column.count("1")
    zero_count = current_column.count("0")
    if one_count >= zero_count:
        winner = "1"
    else:
        winner = "0"
    return filter_oxygen(list(filter(partial(check_col, col, winner), binary_lines)), col+1)

def filter_co2(binary_lines, col=0):
    """Determine most common value in current column"""
    if len(binary_lines) == 1:
        return binary_lines[0]
    current_column = list(map(lambda x: x[col], binary_lines))
    one_count = current_column.count("1")
    zero_count = current_column.count("0")
    if zero_count <= one_count:
        winner = "0"
    else:
        winner = "1"
    # print(one_count, zero_count, winner)
    return filter_co2(list(filter(partial(check_col, col, winner), binary_lines)), col+1)

def check_col(col, goal, bin_str):
    return (bin_str[col] == goal)

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
    return input_list


if __name__ == "__main__":
    input_list = load_input("d03-input.txt")
    column_length = len(input_list[0])

    for col in range(column_length):
        binary_cols.append([])
    
    # a list of lists of the values for each column
    for bin_str in input_list:
        for col_ind in range(len(bin_str)):
            binary_cols[col_ind].append(bin_str[col_ind])

    gamma = ""
    epsilon = ""

    zero_counts = []
    one_counts = []
    for col in range(column_length):
        zero_counts.append(binary_cols[col].count("0"))
        one_counts.append(binary_cols[col].count("1"))
        if zero_counts[col] > one_counts[col]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    print(f"gamma is {int(gamma,2)} and epsilon is {int(epsilon,2)} and together they make {int(gamma,2)*int(epsilon,2)}")
    
    oxygen_rating = filter_oxygen(input_list)
    print(f"winning oxygen string is {oxygen_rating} or {int(oxygen_rating, 2)}")

    co2_rating = filter_co2(input_list)
    print(f"winning co2 string is {co2_rating} or {int(co2_rating, 2)}")

    print(f"live rating is {int(oxygen_rating,2) * int(co2_rating,2)}")


