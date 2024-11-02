## Essential Questions

- How do we make programs that react to their environment?
- Why are conditionals so powerful?

## Lesson Plan

In this lesson, students will be exposed to conditionals for the first time.
They will reflect on their previous experience in Scratch and make connections
with the new material. Finally, they will start to work on the Grok lesson
on if/else.

### Setup up

- Schoology quiz up to Grok Lesson 3.2

### Actual Lesson

- Opening problem
- Give quiz
- Review
    - Strings
    - Integers
    - `input()`
- What is a conditional?
    - Conditionals from real life
        - What are some conditionals you "evaluate" in the morning
            - Ask the class
            - e.g., If cold then put on coat
    - Allows computer programs to react to their environment
- Conditionals
    - Compare to Scratch
    - "evaluates to True"
- Python minutea
    - Location of `:`
    - Spacing
    - `==` vs. `=`
    - Indentation
- Do example of `if`:
    ```python
    x_str = input("Enter a number: ")
    x_int = int(x_str)

    if x_int == 5:
        print("Hello")
        print("...with an exclamation point!")

    print("Bye!")
    ```
- Do example of `if/else`:
    ```python
    x_str = input("Enter a number: ")
    x_int = int(x_str)

    if x_int < 5:
        print("Not a big number")
    else:
    print("Let's see...")
    if x_int <= 5:
        print("Very specific number")
    else:
        print("Starting to be a big number")
        
    print("Done silly example")
    ```
- Go!

#### Homework

- TIL entry on `if` statements
- Finish Grok Lesson 4.2
