#!/usr/bin/env python3

regular_score = 0
insanity_score = 0

# Question 1
print("Do you prefer (a) the mountains or (b) the sea?")
answer1 = input("Enter a or b: ")
if answer1.lower() == "a":
    regular_score += 1

# Question 2
print("Do you like (a) summer or (b) winter?")
answer2 = input("Enter a or b: ")
if answer2.lower() == "a":
    regular_score += 1

# Question 3
print("Do you prefer (a) reading or (b) writing?")
answer3 = input("Enter a or b: ")
if answer3.lower() == "a":
    regular_score += 1

# Question 4
answer4 = input("Do you have the desire to sky dive? ")
if answer4.lower() == "yes":
    insanity_score += 1

if insanity_score != 1:
    # Calculate score to determine personality type
    if regular_score == 0:
        print("""You're a "Creative Thinker"!""")
    elif regular_score == 1:
        print("""You're a "Practical Realist"!""")
    elif regular_score == 2:
        print("""You're an "Innovative Dreamer"!""")
    else:
        print("""You're a "Visionary Leader"!""")
else:
    print("""You're "Insane"!""")
