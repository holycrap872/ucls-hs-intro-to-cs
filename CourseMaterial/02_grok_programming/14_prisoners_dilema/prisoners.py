#!/usr/bin/env python3


################################################################################
# Choices and scoring
################################################################################


def get_score(human_choice, bot_choice):
    if human_choice == "cooperate" and bot_choice == "cooperate":
        # Cooperation!
        return 3, 3
    elif human_choice == "defect" and bot_choice == "cooperate":
        # We tricked them!
        return 5, 0
    elif human_choice == "cooperate" and bot_choice == "defect":
        # They tricked us!
        return 0, 5
    else:
        return 1, 1


################################################################################
# Bots!!
################################################################################


def get_mother_theresa_bot_choice(human_choices):
    return "cooperate"


def get_devil_bot_choice(human_choices):
    return "defect"


def get_con_man_bot_choice(human_choices):
    if len(human_choices) == 4:
        return "defect"

    return "cooperate"


def get_opposite_day_bot_choice(human_choices):
    raise NotImplementedError


################################################################################
# Humanity's last hope!
################################################################################


def get_human_choice(bot_choices):
    return "defect"


################################################################################
# Game loop
################################################################################
def play():
    human_choices = []
    human_total_score = 0

    bot_choices = []
    bot_total_score = 0

    for round_num in range(5):
        human_choice = get_con_man_bot_choice(bot_choices)
        bot_choice = get_mother_theresa_bot_choice(human_choices)

        human_round_score, bot_round_score = get_score(human_choice, bot_choice)

        human_total_score += human_round_score
        bot_total_score += bot_round_score

        bot_choices.append(bot_choice)
        human_choices.append(human_choice)

        print(f"Results of round {round_num}... Human Score: {human_round_score}, Bot Score: {bot_round_score}")

    print(f"Total Human Score: {human_total_score}, Total Bot Score: {bot_total_score}")


if __name__ == "__main__":
    play()
