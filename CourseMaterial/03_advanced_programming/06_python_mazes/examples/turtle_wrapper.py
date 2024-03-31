#!/usr/bin/env python3
import os
import time
import turtle
import typing

from turtle_levels import FILE_TO_LEVEL_MAP, get_color

CONFIG_DICT = {}


FILE_NAME_KEY = "filename"
TARGET_LIST_KEY = "target_list"
SPEED_KEY = "speed"


def __handle_speed():
    speed: int = CONFIG_DICT[SPEED_KEY]
    if speed != 0:
        wait = (6 - speed) * 0.1
        time.sleep(wait)


def _get_color(x: int, y: int) -> typing.Optional[str]:
    file_name = CONFIG_DICT[FILE_NAME_KEY]
    level_data = FILE_TO_LEVEL_MAP[file_name]

    box_size = 50
    num_rows = len(level_data)
    num_columns = len(level_data[0])

    total_width = num_columns * box_size
    total_height = num_rows * box_size

    relative_x = (total_width / 2) + x
    relative_y = (total_height / 2) - y

    # Calculate column and row indices
    if 0 <= relative_x < total_width:
        column_index = int(relative_x / box_size)
    else:
        return None  # Horizontally outside the grid

    if 0 <= relative_y < total_height:
        row_index = int(relative_y / box_size)
    else:
        return None  # Vertically outside the grid

    return get_color(level_data[row_index][column_index])


def init_maze(background_path: str, *, x: int, y: int, speed: int) -> None:
    file_name = os.path.basename(background_path)
    CONFIG_DICT[FILE_NAME_KEY] = file_name
    CONFIG_DICT[SPEED_KEY] = speed

    turtle.bgpic(background_path)

    # bring the turtle to the starting point
    turtle.penup()
    turtle.clear()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.speed(speed)


def forward(num_pixels: int) -> None:
    __handle_speed()
    turtle.forward(num_pixels)


def left(degrees: int) -> None:
    __handle_speed()
    turtle.left(degrees)


def right(degrees: int) -> None:
    __handle_speed()
    turtle.right(degrees)


def on_red() -> bool:
    assert FILE_NAME_KEY in CONFIG_DICT

    x, y = turtle.pos()
    return _get_color(int(x), int(y)) == "red"
