#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 11: Dumbo Octopus

Original problem at https://adventofcode.com/2021/day/2

"""

oct_grid = []

def oct_step():
    """"""
    global grid
    flashers = set()
    flashed = set()
    # increment all
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                flashers.add((x, y))
    # print("before flashing", list(map(get_target, list(flashers))))
    # loop while flashers - flashed
    while len(flashers - flashed) > 0:
        # for flash in flashers:
        for flasher in (flashers - flashed):
            increment_friends(flasher)
            # increment friends
            flashed.add(flasher)
        # print("internal", len(flashers), grid[0])
        # check friends for new flashers
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] > 9:
                    flashers.add((x, y))
    for flasher in flashed:
        x, y = flasher
        grid[x][y] = 0
    # print("after flashing", list(map(get_target, list(flashers))))
    return len(flashers)

def get_target(xy):
    x, y = xy
    return grid[x][y]

def increment_friends(xy):
    global grid
    x, y = xy
    xs = []
    ys = []
    if (x - 1 >= 0):
        xs.append(x - 1)
    xs.append(x)
    if (x + 1 < len(grid)):
        xs.append(x + 1)
    if (y - 1 >= 0):
        ys.append(y - 1)
    ys.append(y)
    if (y + 1 < len(grid[0])):
        ys.append(y + 1)
    for tarx in xs:
        for tary in ys:
            if not (tarx == x and tary == y):
                grid[tarx][tary] += 1

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(list(map(int, line.strip())))
    return input_list

if __name__ == "__main__":
    grid = load_input("d11-input.txt")

    size_of_grid = sum(list(map(len, grid)))

    flashes = 0

    print(grid)
    for i in range(100):
        new_flashes = oct_step()
        if new_flashes == size_of_grid:
            print(f"{new_flashes}, {i}")
        flashes += new_flashes
        print(grid, flashes)
    for i in range(100,1000):
        new_flashes = oct_step()
        if new_flashes == size_of_grid:
            print(f"{new_flashes}, {i+1}")
            break
        flashes += new_flashes
        print(grid, flashes)