def meanie(my_choices, other_choices):
    return "defect"


def tit_for_tat(my_choices, other_choices):
    if len(my_choices) == 0:
        return "cooperate"
    else:
        return other_choices[-1]


def conman(my_choices, other_choices):
    if len(my_choices) == 0:
        return "cooperate"
    elif len(my_choices) == 4:
        return "defect"
    else:
        return other_choices[-1]


def play_game(rounds, bot_0, bot_1):
    b0_score = 0
    b1_score = 0

    b0_choices = []
    b1_choices = []

    for i in range(rounds):
        b0_choice = bot_0(b0_choices, b1_choices)
        b1_choice = bot_1(b1_choices, b0_choices)
        assert b0_choice in ["cooperate", "defect"]
        assert b1_choice in ["cooperate", "defect"]

        if b0_choice == "cooperate" and b1_choice == "cooperate":
            b0_score = b0_score + 3
            b1_score = b1_score + 3
        elif b0_choice == "cooperate" and b1_choice == "defect":
            b0_score = b0_score + 0
            b1_score = b1_score + 5
        elif b0_choice == "defect" and b1_choice == "cooperate":
            b0_score = b0_score + 5
            b1_score = b1_score + 0
        else:
            b0_score = b0_score + 1
            b1_score = b1_score + 1

        print(f"Rnd {i} Bot 0: {b0_choice} - Bot 1: {b1_choice}")
        b0_choices.append(b0_choice)
        b1_choices.append(b1_choice)

    print(f"Final Bot 0: {b0_score} - Bot 1: {b1_score}")
    return [b0_score, b1_score]


def run_tournament():
    bots = [meanie, tit_for_tat, conman]
    scores = []
    for bot in bots:
        scores.append(0)

    for i in range(len(bots)):
        for j in range(len(bots)):
            result = play_game(5, bots[i], bots[j])

            scores[i] = scores[i] + result[0]
            scores[j] = scores[j] + result[1]

    print(scores)


if __name__ == "__main__":
    run_tournament()
