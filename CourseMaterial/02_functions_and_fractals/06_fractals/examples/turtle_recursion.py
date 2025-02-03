from turtle import *


def draw_step(over, up):
    forward(over)
    left(90)
    forward(up)
    right(90)
    draw_step(over, up)
    return "all_done"


penup()
goto(-100, -100)
pendown()
draw_step(30, 10)
