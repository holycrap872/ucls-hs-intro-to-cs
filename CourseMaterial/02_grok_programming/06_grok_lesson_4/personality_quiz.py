#!/usr/bin/env python3

score = 0

# Question 1
print("Do you prefer (a) the mountains or (b) the sea?")
answer1 = input("Enter a or b: ")
if answer1.lower() == "a":
    score += 1

# Question 2
print("Do you like (a) summer or (b) winter?")
answer2 = input("Enter a or b: ")
if answer2.lower() == "a":
    score += 1

# Question 3
print("Do you prefer (a) reading or (b) writing?")
answer3 = input("Enter a or b: ")
if answer3.lower() == "a":
    score += 1

# Calculate score to determine personality type
if score == 0:
    print("You are a Creative Thinker!")
elif score == 1:
    print("You are a Practical Realist!")
elif score == 2:
    print("You are an Innovative Dreamer!")
else:
    print("You are a Visionary Leader!")
