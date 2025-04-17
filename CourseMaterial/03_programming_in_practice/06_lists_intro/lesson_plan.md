## Essential Questions

- What are lists are how are they useful?
- How are lists similar to strings?

## Lesson Plan

### Setup

- `Python Lists One Worksheet` posted to Schoology
    - https://docs.google.com/document/d/1R7hoFZN1GLhcQP5pjsA7wAkP0vrvYi7KMlhexvfcFOM
- Schoology Assessment on lists posted to Schoology
    - See `assessment.md`

### Actual Lesson

- Opening Problem
    ```python
    #!/usr/bin/env python
    def do_something_0(x):
        acc = 1
        for i in range(x):
            acc = acc * 2

        return acc


    if __name__ == "__main__":
        result = do_something_0(8)
        print(result)
    ```
    - What does it print out?
    - Where have we seen 256 before?
    - How to use breakpoints on this
- Review
    - Functions
    - Loops
    - Turbozzle
- Thoughts on Turbozzle
    - Visualize loops/recursion
    - Visualize breakpoints
    - Experience larger program
    - What are your thoughts?
- Lists
    - Purpose of lists:
        - Bundles multiple things together
        - Replaces the need for multiple related variables
- String vs. list comparison
    - Each composed of individual elements
        - characters -> strings, items/elements -> list
    - List slicing vs. string slicing
    - List iteration vs. string iteration
    - Only difference is can append
- Example (if long block)
    ```python
    def do_something(words):
        count = 0
        for word in words:
            if "e" in word.lower():
                count += 1

        return count

    if __name__ == "__main__":
        result = do_something(["hey", "there", "you"])
        print(result)
    ```
- Setup worksheet
    - Each person needs their own version
    - Work next to whomever you'd like
- Go!

### Homework

- Schoology assessment on lists
- TIL entry on lists vs. strings
