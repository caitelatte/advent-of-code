#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 7: The Treachery of Whales!

Original problem at https://adventofcode.com/2021/day/7

"""

import math as maths

def mean_crabs(crabs_list):
    return sum(crabs_list)/len(crabs_list)

def median_crabs(crabs_list):
    midpoint = len(crabs_list)/2
    median = (crabs_list[maths.floor(midpoint)] + crabs_list[maths.ceil(midpoint)]) / 2
    return median

def fuel_cost(crabs_list, goal):
    # print(list(zip(crabs_list,map(lambda x: abs(x - goal), crabs_list))))
    return sum(map(lambda x: abs(x - goal), crabs_list))

def advanced_fuel_cost(crabs_list, goal):
    cost_list = list(map(lambda x: sum(range(0,abs(x - goal)+1)), crabs_list))
    # print(goal, sum(cost_list), list(zip(crabs_list,cost_list)))
    return sum(cost_list)

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = list(map(int,input_file.readline().split(",")))
    return input_list

if __name__ == "__main__":
    crabs_list = sorted(load_input("d07-input.txt"))
    print(f"is it {mean_crabs(crabs_list)}")
    print(f"what about {median_crabs(crabs_list)}")
    print(f"median takes {fuel_cost(crabs_list, median_crabs(crabs_list))} fuel")
    # try the min fuel cost of the quartile around the median
    mid_quartile = range(maths.floor(len(crabs_list)*0.2),maths.ceil(len(crabs_list)*0.8))
    costs = {}
    for goal in mid_quartile:
        costs[goal] = fuel_cost(crabs_list, goal)
    min_goal = min(costs, key=costs.get)
    print(f"min fuel cost of median quartile is {min_goal} which costs {costs[min_goal]}")


    fancy_costs = {}
    for goal in range(maths.floor(len(crabs_list)*0.2),maths.ceil(len(crabs_list)*0.8)):
        fancy_costs[goal] = advanced_fuel_cost(crabs_list, goal)
    min_fancy_goal = min(fancy_costs, key=fancy_costs.get)
    print(f"min fuel cost of median quartile is {min_fancy_goal} which costs {fancy_costs[min_fancy_goal]}")
