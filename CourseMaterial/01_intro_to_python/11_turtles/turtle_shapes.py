import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("blue")
t.speed(0)


# 9
# for i in range(8):
#     for j in range(3):
#         t.forward(10)
#         t.right(120)
#     t.left(45)
#     t.forward(40)

# size = 5
# for i in range(0, 40):
#     t.forward(size)
#     t.left(90)
#     size += 5
# 




# print(dir(t))


# 11
# for i in range(6):
#     for i in range(3):  # Loop 36 times
#         t.forward(20)   # Move forward by 100 units
#         t.right(120)     # Turn right by 170 degrees
#     t.penup()
#     t.forward(100)
#     t.right(60)
#     t.pendown()


# Bonus 1
# for i in range(8):
#     for j in range(60):
#         t.forward(1)
#         t.right(1)
#     t.goto(0,0)
#     t.left(15)
    
# Bonus 2
for i in range(18):
    t.penup()
    t.forward(90)
    t.pendown()
    for j in range(4):
        t.forward(10)
        t.right(90)
    t.penup()
    t.forward(25)
    t.pendown()
    for j in range(4):
        t.forward(10)
        t.right(90)
    t.penup()
    t.backward(115)
    t.right(20)

# Bonus 3
# size = 1
# for i in range(1000):
#     t.forward(size)
#     t.right(20)
#     size += 1
# 
# # End the program
# screen.exitonclick()


# Bonus 4
# size = 1
# for i in range(1000):
#     t.forward(size)
#     t.right(20)
#     size += 1
screen.exitonclick()