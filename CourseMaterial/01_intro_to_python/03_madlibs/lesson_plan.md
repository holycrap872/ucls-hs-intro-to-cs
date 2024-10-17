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

- Students enrolled in "Turtle Playground" course
- `Python Strings Worksheet` loaded in Schoology
    - https://docs.google.com/document/d/1-AwvVtv59yDz-mvorbLMAJdnjadjgOmC5QAquUhNyp0

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
- Mad Libs
    - Do example
    ```python
    name = input("Enter a name: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    number_str = input("Enter a number: ")
    number_int = int(number_str)

    print(f"{name} walked into the forest looking for a normal {animal}.")
    print(f"Instead, {name} got more than they could handle with {number_int}")
    print(f"{color} {animal}s who were looking very hungry! {name} knew")
    print(f"they could handle {number_int - 1} {animal}s, but {number_int} was")
    print(f"one too many, so {name} ran away very quickly.")
    ```
- Have them do Mad Libs in pairs
    - Once finish, rotate and do another group's
    - Must have:
        - A variable that take a string and uses it
        - A variable that takes a number and adds it to another number
        - A quotation from someone famous (in quotes)
- Break
- Grok

#### Homework

- TIL entry in the `int()` function
- Prep for quiz

#### Extensions

- ASCII art
    - https://projects.raspberrypi.org/en/projects/about-me/6
