## Essential Questions

- How do computer programs interact with users?
- What can we assume about incoming data?

## Lesson Plan

In this lesson, we introduce student's to the `int()` function, talk about
how it is used, and compare it with the `input` function. In particular, we
focus on how we can manipulate the data returned by a user however we'd like.
To drive the point home, students then make their own Mad Libs and share them
amongst themselves.

### Setup

- Students enrolled in "Playground - Turtle Python" course
- `Python Strings Worksheet` loaded in Schoology
    - https://docs.google.com/document/d/1WiPOm2rhkvlUwcjVRlnW2JvUplX-uTHkN4JJL3AG09Q
- Tab to "Playground - Turtle Python" open in two tabs
    - https://groklearning.com/learn/python-turtle-playground/1/2/
    - tab 1: Filled with double age (see below)
    - tab 2: Filled with Mad Lib (see below)

### Actual Lesson

- Review
    - Grok stuff
        - input
        - f-string
- TIL Entries
    - Find some good ones and put into slide show
- Talk `input()`
    - Returns a string, so what does "please enter a number" entail?
    - `int()` function
    - Do example
    ```python
    num_1 = input("Enter a number? ")
    num_2 = input("Enter a second number? ")
    print(f"The sum is: {num_1 + num_2}")
    ```
- Mad Libs
    - Do example
    ```python
    exclamation = input("Enter an exclamation: ")
    adverb = input("Enter an adverb: ")
    animal = input("Enter an animal: ")
    number_1_str = input("Enter a number: ")
    number_1_int = int(number_1_str)

    print(f'"{exclamation}!" they said {adverb} as they jumped into their car')
    print(f"with their {number_1_int} big {animal}s. All {number_1_int + 2} of")
    print("them drove of very happily.")
    ```
- Have them do Mad Libs in pairs (?)
    - Once finish, rotate and do another group's
    - Must have:
        - A variable that take a string and uses it
        - A variable that takes a number and adds it to another number
        - A quotation from someone famous (in quotes)
- Break
- Grok

### Homework

- TIL entry in the `int()` function
- Prep for quiz

### Extensions

- ASCII art
    - https://projects.raspberrypi.org/en/projects/about-me/6
