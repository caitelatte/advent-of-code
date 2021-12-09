#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 6: Lanternfish

Original problem at https://adventofcode.com/2021/day/6

"""

def process_fish(fish_list):
    """Given a list of fish, age them by a day."""
    new_fish = 0
    for f in range(len(fish_list)):
        if fish_list[f] == 0:
            new_fish += 1
            fish_list[f] = 6
        else:
            fish_list[f] -= 1
    for nf in range(new_fish):
        fish_list.append(8)
    return fish_list

def smart_process_fish(fish_list, days):
    """Given a list of fish, split it out into age indexes and process."""
    fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for f in fish_list:
        fish_dict[f] += 1
    for day in range(days):
        new_fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        # special cases for babying fish
        new_fish_dict[8] += fish_dict[0]
        new_fish_dict[6] += fish_dict[0]
        for i in range(1,9):
            new_fish_dict[i-1] += fish_dict[i]
        fish_dict = new_fish_dict
    return fish_dict

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = list(map(int, input_file.readline().split(",")))
    return input_list

if __name__ == "__main__":
    fish_list = load_input("d06-input.txt")
    fish_list_80 = fish_list.copy()
    for day in range(80):
        fish_list_80 = process_fish(fish_list_80)
    print(f"after 80 days there are {len(fish_list_80)} fish")
    fish_list_256 = fish_list.copy()

    # bruteforce (this takes way too long)
    # for day in range(256):
    #     fish_list_256 = process_fish(fish_list_256)
    # print(f"after 256 days there are {len(fish_list_256)} fish")

    # bucket process
    bucket_fish_list_80 = smart_process_fish(fish_list, 80)
    print(f"after 80 days there are {sum(bucket_fish_list_80.values())} fish")
    # bucket process
    bucket_fish_list_256 = smart_process_fish(fish_list, 256)
    print(f"after 256 days there are {sum(bucket_fish_list_256.values())} fish")