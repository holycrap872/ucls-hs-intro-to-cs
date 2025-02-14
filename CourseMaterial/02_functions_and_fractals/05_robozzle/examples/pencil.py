def ask_alondra():
    return "pencil"


def ask_bruce():
    hand_bruce = ask_alondra()
    return hand_bruce


def ask_chris():
    hand_chris = ask_bruce()
    return hand_chris


if __name__ == "__main__":
    print("Could you hand me that pencil?")
    hand_mr_rizzi = ask_chris()
    print(f"Thanks for the {hand_mr_rizzi}")
