from turtle import *


def do_something_1(num_levels):
    if num_levels <= 0:
        forward(15)
    else:
        forward(15)
        left(90)
        forward(15)
        backward(15)
        right(90)
        do_something_1(num_levels - 1)


do_something_1(3)
