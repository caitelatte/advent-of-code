#! /usr/local/bin/python3
# Caitlin Macleod

"""AoC 2018 Day 1: Chronal Calibration

Part one: 

Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

Part two:

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.
"""

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        freq_list = []
        for line in input_file:
            freq_list.append(int(line.strip()))
    return freq_list

if __name__ == "__main__":
    freq_list = load_input("d01-input.txt")

    # Find part one
    current_freq = 0
    for freq in freq_list:
        current_freq += freq
    print(f"The first answer is: f{current_freq}")

    # Find part two: 
    current_freq = 0
    past_freqs = set([current_freq])
    first_dup_freq = None
    while first_dup_freq is None:
        for freq in freq_list:
            current_freq += freq
            if current_freq in past_freqs:
                first_dup_freq = current_freq
                break
            else:
                past_freqs.add(current_freq)
    print(f"The first duplicate is: f{first_dup_freq}")