#!/usr/bin/env python3
def prisoner_bot(my_choices, other_choices):
    if len(my_choices) == 0:
        return "defect"
    elif "defect" in other_choices:
        return "defect"
    else:
        return "cooperate"


if __name__ == "__main__":
    # Round 1
    round_1 = prisoner_bot([], [])
    print(round_1)
    # Round 2
    round_2 = prisoner_bot(["defect"], ["cooperate"])
    print(round_2)
