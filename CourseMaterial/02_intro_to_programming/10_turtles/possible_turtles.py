from turtle import *

colours = ["red", "green", "blue", "orange", "pink", "purple"]
speed(0)
for x in range(360):
    pencolor(colours[x % 6])
    width(x // 100 + 1)
    forward(x)
    left(59)
