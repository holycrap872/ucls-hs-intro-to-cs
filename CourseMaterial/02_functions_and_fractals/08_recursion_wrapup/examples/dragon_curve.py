from turtle import *


def build_dragon_string(level):
    if level == 0:
        return ""

    # Get the previous pattern
    previous = build_dragon_string(level - 1)

    # Make current pattern by:
    # 1. Using previous pattern
    # 2. Adding "L" for fold
    # 3. Using previous pattern with R's and L's flipped
    flipped = ""
    for turn in previous:
        flipped = turn + flipped

    reversed_and_flipped = ""
    for turn in flipped:
        if turn == "L":
            reversed_and_flipped += "R"
        else:
            reversed_and_flipped += "L"

    return previous + "L" + reversed_and_flipped


instructions = build_dragon_string(6)
print(instructions)
