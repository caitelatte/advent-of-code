#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 5: Hydrothermal Venture

Original problem at https://adventofcode.com/2021/day/5

"""

from collections import defaultdict
import re

graph = defaultdict(int)
coords_re = r"([\d]+),([\d]+) -> ([\d]+),([\d]+)"
straight_lines = []
diag_lines = []
max_side = 0

def load_input(input_name):
    """Load the input file (a list of line coordinates)."""
    global straight_lines
    global diag_lines
    global max_side
    with open(input_name) as input_file:
        for line in input_file:
            linematch = re.match(coords_re, line)
            (x1, y1, x2, y2) = (int(linematch[1]), int(linematch[2]), int(linematch[3]), int(linematch[4]))
            if (x1 == x2 or y1 == y2):
                straight_lines.append([x1, y1, x2, y2])
            else:
                diag_lines.append([x1, y1, x2, y2])
            max_side = max(x1, x2, y1, y2, max_side)

def plot_line(line):
    """Draw a straight line in the graph"""
    (x1, y1, x2, y2) = line
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            graph[(x1, y)] += 1
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            graph[(x, y1)] += 1
    else:
        print(f"from {x1, y1} to {x2, y2}")
        x_distance = x2 - x1
        y_distance = y2 - y1
        abs_distance = abs(x_distance) + 1

        if x_distance > 0 and y_distance > 0:
            for offset in range(abs_distance):
                graph[(x1 + offset, y1 + offset)] += 1
        elif x_distance > 0 and y_distance < 0:
            for offset in range(abs_distance):
                graph[(x1 + offset, y1 - offset)] += 1
        elif x_distance < 0 and y_distance > 0:
            for offset in range(abs_distance):
                graph[(x1 - offset, y1 + offset)] += 1
        elif x_distance < 0 and y_distance < 0:
            for offset in range(abs_distance):
                graph[(x1 - offset, y1 - offset)] += 1



def plot_graph():
    for x in range(10):
        line_str = ""
        for y in range(10):
            line_str += str(graph[(y,x)])
        print(line_str)

if __name__ == "__main__":
    load_input("d05-input.txt")
    for str_line in straight_lines:
        plot_line(str_line)
    # plot_graph()
    print(f"just using straiht lines, there are {len(graph) - list(graph.values()).count(1) - list(graph.values()).count(0)}")
    for str_line in diag_lines:
        plot_line(str_line)
    # print(sorted(graph))
    plot_graph()
    print(f"using diag lines as well, there are {len(graph) - list(graph.values()).count(1) - list(graph.values()).count(0)}")