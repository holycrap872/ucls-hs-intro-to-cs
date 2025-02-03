import time
from turtle import *


def do_something_2(cur_size, num_levels):
    if num_levels <= 1:
        forward(cur_size)
        back(cur_size)
    else:
        forward(cur_size)
        left(30)
        do_something_2(cur_size / 2, num_levels - 1)
        right(60)
        do_something_2(cur_size / 2, num_levels - 1)
        left(30)
        back(cur_size)


# speed(0)  # Uncomment this line to make the turtle go fast
do_something_2(100.0, 1)
time.sleep(10)
