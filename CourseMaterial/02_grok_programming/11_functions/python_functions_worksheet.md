# Python Functions Worksheet

Instructions:
- Log into Grok
- Go to https://groklearning.com/learn/python-turtle-playground/1/0/
- Read the directions for each task very carefully before you begin working on it.
- Every time the directions say "take a screenshot" of something, do it and then copy it into the proper space _in this document_.

---

This worksheet is intended to be both an introduction to functions and to refresh your memory on what you have learned so far in Python. Work through each task with the help of a partner (being sure to type/run each bit of code yourself).

## Problem 1

Use the code below to answer the following questions and complete the required tasks.

```
def do_something_0(x, y):
    z = x + y
    return z

result = do_something_0(5, 6)
result = do_something_0(4, 2)
print(result)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `do_something_0()` function are there? What is the type (e.g., string or int) of each input?

>

What is the output/result of the function (if any) and what is its type?

>

What do you think will be printed to the screen when you run the code?

>

If you didn’t have the last three lines of the program, what would happen when you run the code? Why?

>

**NEXT**, copy the code into Grok and run it. Look under the **output tab** for the results. 

Were your predictions correct? If not, what mistakes did you make?

>

What would be a better name for the function than `do_something_0()`?

>

One of the lines of code in the program is "unnecessary". Which one?

>

Modify **the body of the function** so it does multiplication rather than addition. Then, modify **the body of the function** so that if the result of the multiplication is greater than 1000, the program prints out "whoa, big number!".

A "function call" is where you call/invoke the function (I do this on the second and third to last lines of the program above). Create two "function calls" of your own below my function calls. One of your function calls should result in the "whoa" being printed out and one should not. Run the code to make sure it does what you expect it to do.

Take a screenshot of **your code in Grok** (including the changes from the previous questions) and paste it here.

## Problem 2

Use the code below to answer the following questions and complete the required tasks.

```
def do_something_1(x):
    output = ""
    for i in range(0, x, 2):
        output = output + str(i) + ", "
    return output + "who do we appreciate?"

result = do_something_1(10)
print(result)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `do_something_1()` function are there? What is the type (e.g., string or int) of each input?

>

What is the output/result of the function (if any) and what is its type?

>

What do you think will be printed to the screen when you run the code?

>

**NEXT**, copy the code into the Grok window and run it.

Were your predictions correct? If not, what mistakes did you make?

>

What would be a better name for the function than `do_something_1()`?

>

Modify the body of the function so that it **starts** the cheer at the number 2.

Modify the body of the function so that it **includes** the number that was given as the input to the function in its cheer.

This code is an example of the "accumulator pattern". Why?

>

Take a screenshot of **your code in Grok** (including the changes from the previous questions) and paste it here.

## Problem 3

Use the code below to answer the following questions and complete the required tasks.

```
from turtle import *

def make_shape(x):
    for i in range(4):
        forward(x)
        left(90)

make_shape(30)
make_shape(60)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `make_shape()` function are there? What is the type (e.g., string or int) of each input?

>

What is the output/result of the function (if any) and what is its type?

>

What do you think will be printed to the screen when you run the code?

>

**NEXT**, copy the code into the Grok window and run it.

Were your predictions correct? If not, what mistakes did you make?

>

What would be a better name for the input variable than `x`?

>

Alter the body of the function to make it create a triangle. What specifically did you change?

>

Alter the body of the function to make it create a hexagon. What specifically did you change?

>

Alter the function so it has another input (`num_sides`) that determines the number of sides a shape should have. Then, alter the body of the function so it uses that input to create the desired shape. For example, `make_shape(100, 8)` should make an octagon that has sides of length 100. Note: the trick is to turn 360 / num_sides at each side. Test your function with 2 calls.

Take a screenshot of **your code in Grok** and paste it here.

(Optional: 5 bonus points on quiz) **Outside of the function**, call the `make_shape()` function in a loop so that you create multiple shapes with 3 - 20 sides. Take a screenshot of **the resulting image** and paste it here.

## Problem 4 (Optional: 5 bonus points on quiz)

Functions can call themselves. This is called recursion. Use the recursive code below to answer the following questions and complete the required tasks.

```
def call_me(num):
    if num == 0:
        print("All done")
    else:
        print(num)
        call_me(num - 1)

call_me(10)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `call_me()` function are there? What is the type (e.g., string or int) of each input?

>

What is the output/result of the function (if any) and what is its type?

>

Based on the definition of recursion above, why is the `call_me()` function considered recursive?

>

What do you think will happen when you run the code?

>

**NEXT**, copy the code into the Grok window and run it.

Was your prediction correct? If not, what mistake did you make?

>

The bit of code that checks for n == 0 is called the "base case". Why is the base case necessary?

>

Alter the body of the function so that it counts **UP** to a given number. Take a screenshot of **your code in Grok** and paste it here.
