#!/usr/bin/env python3
from turtle_wrapper import *


def solve_maze_0() -> None:
    init_maze("CourseMaterial/03_advanced_programming/06_python_mazes/examples/maze_0.png", x=-175, y=0, speed=1)

    for i in range(12):
        if on_red():
            left(90)
        forward(50)


if __name__ == "__main__":
    solve_maze_0()
