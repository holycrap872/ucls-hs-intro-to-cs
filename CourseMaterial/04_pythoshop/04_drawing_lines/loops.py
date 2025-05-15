import turtle

turtle.colormode(255)

SQUARE_SIZE = 22
START_X = -300
START_Y = 300
PROG_X = 100
PROG_Y = 180

colorGrid = [
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (255, 160, 0),
    (255, 160, 0),
    (255, 160, 0),
    (255, 160, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (255, 160, 0),
    (255, 160, 0),
    (255, 160, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (255, 160, 0),
    (255, 160, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (255, 160, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 0, 75),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 75, 160),
    (0, 75, 160),
    (0, 0, 75),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 75, 160),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 75),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 75, 160),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 75),
    (0, 0, 0),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 75),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 255),
    (0, 0, 75),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (75, 255, 255),
    (75, 255, 255),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 255),
    (0, 0, 75),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 75),
    (0, 75, 160),
    (0, 75, 160),
    (0, 0, 255),
    (0, 0, 75),
    (0, 0, 75),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
    (0, 0, 255),
]


def realX(x, flip=False) -> int:
    if flip == False:
        return (x * SQUARE_SIZE) + START_X
    else:
        return (START_X - (SQUARE_SIZE * x)) + (SQUARE_SIZE * 15)


def realY(y) -> int:
    return (START_Y - (SQUARE_SIZE * 16)) + (y * SQUARE_SIZE)


def nextPixel() -> None:
    global continueLoop
    continueLoop = True


def allPixels() -> None:
    global ignoreStop
    ignoreStop = True


continueLoop = False
ignoreStop = False

turtle.onkey(nextPixel, "space")
turtle.onkey(allPixels, "a")

# draws lines
numWriter = turtle.Turtle()
numWriter.penup()
numWriter.hideturtle()
# writes code
progWriter = turtle.Turtle()
progWriter.penup()
progWriter.hideturtle()

# stamps the squares
sq = turtle.Turtle()
sq.speed(0)
sq.penup()
sq.shape("square")
sq.color(255, 0, 0)


turtle.tracer(0)
# number the axes
for x in range(16):
    numWriter.goto(realX(x), realY(0) + 11)
    numWriter.write(x, move=False, align="center", font=("Arial", 16, "normal"))
for y in range(14):
    numWriter.goto(START_X - 13, realY(y) - 9)
    numWriter.write(y, move=False, align="right", font=("Arial", 16, "normal"))

# draw orig pic
colorGrid.reverse()
for y in range(14):
    for x in range(16):
        sq.color(colorGrid[y * 16 + x])
        sq.goto(realX(x, flip=True), realY(y))
        sq.stamp()
turtle.update()


# write starting program
progWriter.goto(PROG_X, PROG_Y)
progWriter.write(f"w = get_width(image)", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 30)
progWriter.write(f"h = get_height(image)", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 60)
progWriter.write("for y in range(h):", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 90)
progWriter.write("   for x in range(w):", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 120)
progWriter.color(128, 128, 128)
progWriter.write(
    "      set_pixel_rgb(image, (x, y), (255, 0, 0))", move=False, align="left", font=("Arial", 24, "normal")
)
progWriter.color(0, 0, 0)
turtle.update()

turtle.listen()
# after space bar, update program
while not continueLoop:
    turtle.update()
continueLoop = False
progWriter.clear()
progWriter.goto(PROG_X, PROG_Y)
progWriter.write(f"w = 16", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 30)
progWriter.write(f"h = 14", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 60)
progWriter.write("for y in range(h):", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 90)
progWriter.write("   for x in range(w):", move=False, align="left", font=("Arial", 24, "normal"))
progWriter.goto(PROG_X, PROG_Y - 120)
progWriter.write(
    "      set_pixel_rgb(image, (x, y), (255, 0, 0))", move=False, align="left", font=("Arial", 24, "normal")
)
turtle.update()

# use space bar to go through nested for loop
for y in range(14):
    for x in range(16):
        while not continueLoop and not ignoreStop:
            turtle.update()
        continueLoop = False
        sq.color(255, 0, 0)
        sq.goto(realX(x), realY(y))
        sq.stamp()
        progWriter.clear()
        progWriter.goto(PROG_X, PROG_Y)
        progWriter.write(f"w = 16", move=False, align="left", font=("Arial", 24, "normal"))
        progWriter.goto(PROG_X, PROG_Y - 30)
        progWriter.write(f"h = 14", move=False, align="left", font=("Arial", 24, "normal"))
        progWriter.goto(PROG_X, PROG_Y - 60)
        progWriter.write(f"for {y} in range(h):", move=False, align="left", font=("Arial", 24, "normal"))
        progWriter.goto(PROG_X, PROG_Y - 90)
        progWriter.write(f"   for {x} in range(w):", move=False, align="left", font=("Arial", 24, "normal"))
        progWriter.goto(PROG_X, PROG_Y - 120)
        progWriter.write(
            "      set_pixel_rgb(image, (x, y), (255, 0, 0))", move=False, align="left", font=("Arial", 24, "normal")
        )
        turtle.update()

# indicate program is done
progWriter.goto(PROG_X, PROG_Y - 120)
progWriter.color(128, 128, 128)
progWriter.write("#done", move=False, align="left", font=("Arial", 24, "normal"))
