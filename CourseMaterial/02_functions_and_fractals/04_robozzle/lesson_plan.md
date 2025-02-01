## Essential Questions

- How do functions actually work?
- What is the "function call stack"?

## Lesson Plan

### Setup

- `Robozzle Worksheet` loaded into Schoology
    - https://docs.google.com/document/d/1QiQHOOVJecKwnOi_IGNrIDqSbMQhL2UCoL90OGBYXFg
- `make_shirt()` example ready to run in vscode
    - ```python
        def make_thread(t):
            print(f"Starting to make {t} thread")
            print(f"Made thread with lots of wool")
            return f"{t} thread"

        def make_cloth(c):
            print(f"Starting to make {c} clothes")
            supplies = make_thread(c * 100)
            print(f"Made cloth with {supplies}")
            return f"{c} cloth"

        def make_shirts(s):
            print(f"Starting to make {s} shirts")
            supplies = make_cloth(s * 3)
            print(f"Made shirt with {supplies}")
            return f"{s} shirt"

        if __name__ == "__main__":
            result = make_shirts(1)
    ```

### Actual Lesson

- Review
    - Python
        - What is programming?
        - Why is it so powerful?
    - Functions
        - What are they?
        - Why are they so powerful?
- Function call stack
    - Program pauses and waits for answer from function
    - Give example
        - Making a shirt requires cloth which requires thread
        - Pause while waiting for delivery
    - Walk through a visual where the fn call pauses while called fn completes
    - Show `make_shirt()` example in vscode
- Today going to play a game to illustrate the function call stack
    - Robozzle
    - If work hard, then shouldn't have any homework
- Demonstration
    - Do simple level
    - Explain how their procedures are similar to python's
        - `Mn` pauses and waits for completion
    - How similar/different to more general programming language?
- Walk through worksheet
- Go!
- Debrief at end
    - Show function call stack for simple level

### Homework

- TIL Entry on the function call stack
