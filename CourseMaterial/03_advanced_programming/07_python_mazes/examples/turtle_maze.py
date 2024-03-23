#!/usr/bin/env python3
from turtle_wrapper import *


# load the appropriate image
def solve_maze_0() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_0.png", -60, 170)

    # write your code below
    forward(100)
    right(90)
    forward(220)
    right(90)
    forward(50)
    left(90)
    forward(130)

    # press enter in the Terminal to exit the program
    input("Press enter when done")


def do_swoosh():
    forward(170)
    left(90)
    forward(350)
    left(180)
    forward(350)
    left(90)


def solve_maze_1() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_1.png", -400, -160)

    # write your code below
    forward(-20)
    for i in range(5):
        do_swoosh()

    # press enter in the Terminal to exit the program
    input("Press enter when done")


def solve_maze_2() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_2.png", -130, -80)

    while True:
        forward(53)
        if on_red():
            left(90)

    input("Press enter when done")


if __name__ == "__main__":
    # solve_maze_0()
    # solve_maze_1()
    solve_maze_2()
