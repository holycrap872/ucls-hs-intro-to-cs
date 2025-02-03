from turtle import *


def dragon(level, direction):
    if level:  # Same as "if level > 0"
        right(direction * 45)
        dragon(level - 1, 1)
        left(direction * 90)
        dragon(level - 1, -1)
        right(direction * 45)
    else:
        forward(10)  # Base length


speed(0)  # Fastest speed
penup()
goto(-100, 0)  # Start position
pendown()
dragon(12, 1)
