# Python Lists Worksheet

Instructions:
- Log into Grok
- Go to https://groklearning.com/learn/python-turtle-playground/1/0/
- Read the directions for each task very carefully before you begin working on it.
- Every time the directions say "take a screenshot" of something, do it and then copy it into the proper space _in this document_.

---

This worksheet is intended to further your understanding of lists and to demonstrate the prisoner’s dilemma game. Work through each task with the help of a partner (being sure to type/run each bit of code yourself).

## Problem 1:

Use the code below to answer the following questions and complete the required tasks.

```
def do_something_0(x, y):
    tracker = 0
    for item in x:
        if item == y:
            tracker = tracker + 1
    return tracker

result = do_something_0([9, 6, 9, 2, 18], 9)
print(result)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `do_something_0()` function are there? What is the type (e.g., list, string, or int) of each input?

>

What is the output/result of the function (if any) and what is its type?

>

What do you think will be printed to the screen when you run the code?

>

If you didn’t have the last two lines of the program, what would happen when you run the code? Why?

>

**NEXT**, copy the code into Grok and run it. Look under the **output tab** for the results. 

Were your predictions correct? If not, what mistakes did you make?

>

The `do_something_0()` function is similar to a function that we learned about that operates on strings. Which function is this?

>

What would be a better name for the function than `do_something_0()`?

>

Modify **the function** so that it takes three inputs: a list, a minimum number, and a maximum number. Then, modify **the body of function** so that it counts the number of items in the list that are between (exclusive) the minimum and the maximum.

A "function call" is where you call/invoke the function. Create two "function calls" of your own below my function call. One or your function calls should result in a `0` being returned (and printed) and another should result in a `2` being returned (and printed).

Take a screenshot of **your code in Grok** and paste it here.

## Problem 2

Now we’re going to get started with the prisoner’s dilemma. Below is code for a two round "game" between two prisoners. Use the code to answer the following questions and complete the required tasks.

```python
def prisoner_bot_0(my_choices, other_choices):
    return "cooperate"

def prisoner_bot_1(my_choices, other_choices):
    return "defect"

b0_score = 0
b1_score = 0

b0_choices = []
b1_choices = []

for i in range(2):
  b0_choice = prisoner_bot_0(b0_choices, b1_choices)
  b1_choice = prisoner_bot_1(b1_choices, b0_choices)
 
  if b0_choice == "cooperate" and b1_choice == "cooperate":
    b0_score = b0_score + 3
    b1_score = b1_score + 3
  elif b0_choice == "defect" and b1_choice == "defect":
    b0_score = b0_score + 1
    b1_score = b1_score + 1
  else:
    b0_score = b0_score + 5
    b1_score = b1_score + 0

  print("Rnd", i, "Bot 0:", b0_choice, "- Bot 1:", b1_choice)
  b0_choices.append(b0_choice)
  b1_choices.append(b1_choice)

print("Final Bot 0:", b0_score, "- Bot 1:", b1_score)
```

**BEFORE** running the program, answer the following questions:

How many inputs to the `prisoner_bot_0()` and `prisoner_bot_1()` functions are there? What is the type (e.g., list, string, or int) of each input?

>

What are the outputs/results of the `prisoner_bot_0()` and `prisoner_bot_1()` functions (if any) and what are their types?

>

What is a better name for `prisoner_bot_0()`? The name should describe its strategy.

>

What is a better name for `prisoner_bot_1()`? The name should describe its strategy.

>

There is a bug in the way the program calculates the score. What is it?

>

What do you think will be printed to the screen when you run the code (without fixing the bug)?

>

**NEXT**, copy the code into Grok and run it.

Were your predictions correct? If not, what mistakes did you make?

>

Modify the code so the game lasts for five rounds.

Fix the bug in the way the program calculates the score. You’ll know that you got it right if the output is `Final Bot 0: 0 - Bot 1: 25`.

Modify the code so the bots’ scores are stored in a list called `scores` rather than in the variables `b0_score` and `b1_score`. Hint: you’ll need `scores = [0, 0]` and `scores[0] = scores[0] + 1`

Take a screenshot of **all of your code modifications** in Grok and paste it here.

## Problem 3

Now we’re going to start modifying the "prisoner bots". Replace **the body** of the `prisoner_bot_0()` function with the following bit of code:

```
if len(other_choices) >= 3:
  return "defect"
else:
  return "cooperate"
```

**BEFORE** running the program, answer the following questions:

What is the strategy of this bot?

>

What is a better name for the `prisoner_bot_0()` function? The name should describe its strategy.

>

What do you think the score will be after five rounds against `prisoner_bot_1()`?

>

**NEXT**, copy the code into Grok and run it.

Were your predictions correct? If not, what mistakes did you make?

>

Alter the body of the function so the bot only cooperates for the first two rounds. What specifically did you change?

>

Alter the body of the function so the bot only cooperates for the first and last round. What specifically did you change?

>

Take a screenshot of **your code for `prisoner_bot_0()` in Grok** and paste it here.

## Problem 4

Now replace **the body** of the `prisoner_bot_1()` function with the following bit of code:

```
if "defect" in other_choices:
  return "defect"
else:
  return "cooperate"
```

**BEFORE** running the program, answer the following questions:

What is the strategy of this bot?

>

What is a better name for the `prisoner_bot_1()` function? The name should describe its strategy.

>

What do you think the score will be after five rounds against the new `prisoner_bot_0()`?

>

**NEXT**, copy the code into Grok and run it.

Were your predictions correct? If not, what mistakes did you make?

>

Alter the body of the function so the bot only defects if the other bot defected **in the first round**. What specifically did you change?

>

Take a screenshot of **your code for `prisoner_bot_1()` in Grok** and paste it here.

## Problem 5 (Optional: 5 point bonus on lowest grade)

Now it’s your turn to create your own bot. You can use a deterministic strategy, a random strategy (via  `random.randint()`), or something of your own making.

**BEFORE** you begin coding, answer the following questions:

Explain in 2-3 sentences the strategy your bot will use:

>

What is a good name for your bot?

>

What do you think the score will be after five rounds against the `prisoner_bot_1()`?

>

**NEXT**, you can begin coding. Create an entirely new function for your bot (using the name you came up with from question 2) right below the two existing prisoner bot functions. Once you’re done, modify the code so you're playing against `prisoner_bot_1()`. Finally, run the code.

Were your predictions correct? If not, what mistakes did you make?

> 

Take a screenshot of **your bot’s code** in Grok and paste it here.

## Problem 6 (Optional: 10 point bonus on lowest grade)

Finally, we’re going to host our own tournament of bots. The rules are pretty simple: 1000 times we’re going to randomly pick two bots to "fight". We’ll sum the scores of each bot over those 1000 "fights"; the winner will be the bot with the highest overall score.

Use the code below to help you answer the following questions and complete the required tasks.

```python
import random

scores = [0, 0, 0]
bots = [prisoner_bot_0, prisoner_bot_1, prisoner_bot_2]

for j in range(1000):
  b0_index = random.randint(0, 2)
  b1_index = random.randint(0, 2)

  b0_choices = []
  b1_choices = []

  for i in range(5):
    b0_choice = bots[b0_index](b0_choices, b1_choices)
    …
```

**BEFORE** running the program, answer the following questions:

What does the keyword `import` mean?

>

What does it mean to `import random`?

>

The lines `b0_index = random.randint(0, 2)` and `b0_choice = bots[b0_index](b0_choices, b1_choices)` are related - and complex. What do you think they do?

>

Explain what your general idea will be for using the code above to help you create an "outer tournament loop".

>

Call your instructor over to verify the previous question.

**NEXT**, you can begin coding. Use the code above to help you create an "outer tournament loop". Once you’re done, run the code.

What was the highest scoring bot?

>

What was the lowest scoring bot?

>

How does using the `b0_index` and `b1_index` variables help us make the program "more general"?

>
