#!/usr/bin/env python3
def person_3(word):
    new_word = word + "d"
    print(f"The word is {new_word}")


def person_2(word):
    new_word = word[:-2]  # all but last two letters
    person_3(new_word)


def person_1(word):
    new_word = word.replace("o", "e")
    person_2(new_word)


def person_0(word):
    new_word = "s" + word
    person_1(new_word)


if __name__ == "__main__":
    person_0("hoot")
