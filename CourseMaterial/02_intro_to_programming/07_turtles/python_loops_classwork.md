# Python Loops Worksheet

Instructions:
1.	Log into Grok
2.	Go to https://groklearning.com/learn/python-turtle-playground/1/0/
3.	Read the directions for each task very carefully before you begin working on it.
4.	Every time the directions say "take a screenshot" of something, do it and then copy it into the proper space _in this document_.

---

This worksheet is intended to be both an introduction to using turtles to draw shapes and an opportunity for you to practice working with loops. Work through each task with the help of a partner (being sure to type/run each bit of code yourself).

## Problem 1:

Use the code below to answer the following questions and complete the required tasks.

```
from turtle import *

# Make a shape
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
```

**BEFORE** running the program, answer the following questions:


1.	What shape do you think this program will draw?

>

2.	Why would modifying the code to use a `for` loop be useful?

>

**NEXT**, copy the code into the Grok window and run it.

1.	Were your predictions correct? If not, what mistakes did you make?

>

2.	There is a comment on line three of the program. What would be a better, more specific comment?

>

3.	Usually, people think of triangles having 60° angles. Why are the angles 120° for turtles?

>

4.	Alter the program so it uses a `for` loop to reduce the total number of lines of code. Take a screenshot of **your code in Grok** and paste it here.

## Problem 2

Now it's time to modify the code you worked on in the previous problem to create a bunch of new shapes.

**BEFORE** modifying the code, answer the following questions:

1. If you **didn't use a loop**, how many lines of code would you need to draw a pentagon?

>

2. What do you think is the **minimal number of changes** needed in your code so that it produces a pentagon rather than a triangle?

>

**NEXT**, modify the code in the Grok window to complete the following tasks.

1. Alter the program so it creates a pentagon. Take a screenshot of **your code in Grok** and paste it here.

2. Were your predictions correct? If not, what mistakes did you make?

>

3. Alter the program so it creates a hexagon. Take a screenshot of **your code in Grok** and paste it here.

4. Alter the program so it creates a five-pointed star. Take a screenshot of **your code in Grok** and paste it here.

5. Alter the program so it uses a `for i in range(100)` to create a cool shape of your own. Take a screenshot of **the resulting image** and paste it here.


## Problem 3

Use the code below to answer the following questions and complete the required tasks.

```
for i in range(8):
    for j in range(3):
        forward(20)
        right(120)
    forward(100)
    right(60)
```

**BEFORE** running the program, answer the following questions:

1. The code above is an example of "nested loops". Why do you think the word "nested" is used?

>

2. What shape do you think the "inner loop" creates?

>

2. What shape do you think the "outer loop" creates?

>

3. When run, what shape do you think the "nested loops" program will draw?

>

**NEXT**, copy the code into the Grok window and run it.

1.	Were your predictions correct? If not, what mistakes did you make?

>

2. In 1-2 sentences, describe a general rule that explain how these types of nested loops work.

>

3. Alter the program so it uses "nested loops" to create a cool shape of your own. Take a screenshot of **your code in Grok** and paste it here.

# Problem 4

Now it's time to write your own code so that the output matches each of the following shapes.

1. SHAPE 1. Take a screenshot of **the resulting image** and paste it here.

1. SHAPE 2. Take a screenshot of **the resulting image** and paste it here.

1. SHAPE 3. Take a screenshot of **the resulting image** and paste it here.

# Problem 5 (Optional: 5 bonus points on quiz)

1. this shape (hint: using t.goto(0, 0) will help)

2. this shape (hint: you will need to use a variable)
