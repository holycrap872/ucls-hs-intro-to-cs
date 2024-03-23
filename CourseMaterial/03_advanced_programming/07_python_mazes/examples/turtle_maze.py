#!/usr/bin/env python3
from turtle_wrapper import *


# load the appropriate image
def solve_maze_0() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_0.png", x=-60, y=170, speed=0)

    # write your code below
    forward(100)
    right(90)
    forward(220)
    right(90)
    forward(50)
    left(90)
    forward(130)


def do_swoosh():
    forward(170)
    left(90)
    forward(350)
    left(180)
    forward(350)
    left(90)


def solve_maze_1() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_1.png", x=-400, y=-160, speed=0)

    # write your code below
    forward(-20)
    for i in range(5):
        do_swoosh()


def solve_maze_2() -> None:
    init_maze("CourseMaterial/03_advanced_programming/07_python_mazes/examples/maze_2.png", x=-130, y=-80, speed=5)

    while True:
        forward(53)
        if on_red():
            left(90)


if __name__ == "__main__":
    # solve_maze_0()
    # solve_maze_1()
    solve_maze_2()
