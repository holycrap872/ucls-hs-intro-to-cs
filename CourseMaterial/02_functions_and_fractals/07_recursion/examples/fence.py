from turtle import *


def do_something_1(size, num_levels):
    if num_levels <= 0:
        forward(size)
    else:
        forward(size)
        left(90)
        forward(size)
        backward(size)
        right(90)
        do_something_1(size, num_levels - 1)


if __name__ == "__main__":
    penup()
    goto(-100, 0)
    pendown()
    do_something_1(30, 3)
