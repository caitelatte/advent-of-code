#! /usr/local/bin/python3
# Caitlin Macleod

"""AoC 2018 Day 4: Repose Record

Part one: 

What is the checksum for your list of box IDs?

Part two:

What letters are common between the two correct box IDs?
"""

import collections
import datetime
import re

time_format = "%Y-%m-%d %H:%M"

action_re = re.compile(r"\[(.+)\] (.+)")
begins_re = re.compile(r"Guard #(\d+) begins shift")
falls_re = re.compile(r"falls asleep")
wakes_re = re.compile(r"wakes up")

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
    return input_list

def parse_action(action):
    action_match = action_re.match(action)
    if action_match is not None:
        action_time = datetime.datetime.strptime(action_match.group(1), time_format)
        action_text = action_match.group(2)
        guard_id = None
        if begins_re.match(action_text):
            guard_id = begins_re.match(action_text).group(1)
    else:
        raise ValueError(f"Action {action} didn't match regex!")
    return {"time": action_time, "text": action_text, "guard": guard_id}

if __name__ == "__main__":
    raw_actions = sorted(load_input("d04-input.txt"))
    actions_list = []
    current_guard_id = None
    for action in raw_actions:
        parsed_action = parse_action(action)
        if parsed_action["guard"] is not None:
            current_guard_id = parsed_action["guard"]
        else:
            parsed_action["guard"] = current_guard_id
        actions_list.append(parsed_action)

    guard_actions = collections.defaultdict(list)
    for g_action in actions_list:
        if falls_re.match(g_action["text"]):
            guard_actions[g_action["guard"]].append((g_action["time"], "falls"))
        elif wakes_re.match(g_action["text"]):
            guard_actions[g_action["guard"]].append((g_action["time"], "wakes"))
    guard_sleeps = collections.defaultdict(list)
    guard_asleep = collections.defaultdict(list)
    guard_totals = {}
    for guard in guard_actions:
        fell_asleep = None
        for g_action in guard_actions[guard]:
            if g_action[1] == "falls":
                fell_asleep = g_action[0]
            elif g_action[1] == "wakes":
                guard_sleeps[guard].append((g_action[0] - fell_asleep).seconds)
                guard_asleep[guard].append((fell_asleep, g_action[0]))
                fell_asleep = None
        guard_totals[guard] = sum(guard_sleeps[guard])
    
    sleepiest_guard = max(guard_totals, key=lambda x: guard_totals[x])

    sg_asleep = guard_asleep[sleepiest_guard]
    asleep_minutes = collections.defaultdict(int)
    for sleep in sg_asleep:
        for minute in range(sleep[0].minute, sleep[1].minute):
            asleep_minutes[minute] += 1
    print(asleep_minutes)
    sleepiest_minute = max(asleep_minutes, key=lambda x: asleep_minutes[x])

    print(f"The sleepiest guard ({sleepiest_guard}) times the sleepiest minute ({sleepiest_minute}) is {int(sleepiest_guard) * sleepiest_minute}")

    