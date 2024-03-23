#!/usr/bin/env python3
import os
import time
import turtle
import typing


class SquareCoord(typing.NamedTuple):
    bottom_left_x: int
    bottom_left_y: int
    top_right_x: int
    top_right_y: int

    def contains(self, x: int, y: int) -> bool:
        if not (self.bottom_left_x <= x <= self.top_right_x):
            return False

        if not (self.bottom_left_y <= y <= self.top_right_y):
            return False

        return True

    @staticmethod
    def get_matching_index(square_coords: typing.List["SquareCoord"], x: int, y: int) -> typing.Optional[int]:
        for i in range(len(square_coords)):
            square_coord = square_coords[i]
            if square_coord.contains(x, y):
                return i

        return None


CONFIG_DICT = {}
RED_SQUARE_COORD_DICT: typing.Dict[str, typing.List[SquareCoord]] = {
    "maze_0.png": [],
    "maze_1.png": [],
    "maze_2.png": [SquareCoord(130, -90, 140, -70)],
}
TARGET_SQUARE_COORD_DICT = {
    "maze_2.png": [SquareCoord(130, 70, 150, 90)],
}

FILE_NAME_KEY = "filename"
TARGET_LIST_KEY = "target_list"


def init_maze(background_path: str, x: int, y: int) -> None:
    file_name = os.path.basename(background_path)
    CONFIG_DICT[FILE_NAME_KEY] = file_name
    CONFIG_DICT[TARGET_LIST_KEY] = TARGET_SQUARE_COORD_DICT[file_name].copy()

    turtle.bgpic(background_path)

    # bring the turtle to the starting point
    turtle.penup()
    turtle.clear()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.speed(5)


def forward(num_pixels: int) -> None:
    time.sleep(0.5)
    turtle.forward(num_pixels)

    target_coord_list: typing.List[SquareCoord] = CONFIG_DICT[TARGET_LIST_KEY]
    x, y = turtle.pos()
    matches = SquareCoord.get_matching_index(target_coord_list, int(x), int(y))

    if matches is not None:
        target_coord_list.pop(matches)

    if not CONFIG_DICT[TARGET_LIST_KEY]:
        print("You win!!!")
        while True:
            turtle.left(10)


def left(degrees: int) -> None:
    time.sleep(0.5)
    turtle.left(degrees)


def right(degrees: int) -> None:
    time.sleep(0.5)
    turtle.right(degrees)


def on_red() -> bool:
    assert FILE_NAME_KEY in CONFIG_DICT
    assert CONFIG_DICT[FILE_NAME_KEY] in RED_SQUARE_COORD_DICT

    square_coords = RED_SQUARE_COORD_DICT[CONFIG_DICT[FILE_NAME_KEY]]
    x, y = turtle.pos()
    return SquareCoord.get_matching_index(square_coords, int(x), int(y)) is not None
