## Essential Questions

- What are functions?
- Why are functions useful?

## Lesson Plan

This lesson serves both as the introduction to functions and as a bit of a
refresher after the winter break. In it, students review everything that they
have covered so far and get a glimpse of where they are going to go in the
upcoming units. After this, the conceptual foundations of functions are
discussed - but no actual Python function terminology since we're relying on
Grok to do this. Finally, students start to work on Grok.

> Note: This lesson somewhat assumes students are just coming back from break

### Setup

- Schoology assessment posted
    - See `assessment.md`

### Actual Lesson

- Opening Problem
    ```python
    word = "relax"
    guess = input("Enter guess: ")
    acc = ""
    for i in range(5):
        guess_letter = guess[i]
        orig_letter = word[i]
        if guess_letter == orig_letter:
            acc = acc + "🟩"
        elif guess_letter in word:
            acc = acc + "🟨"
        else:
            acc = acc + "⬛"
    print(acc)
    ```
- Review
    - What have we done so far?
        - Have student's throw out concepts
            - data types
            - variables
            - functions
            - loops
            - accumulators
- Where are we going?
    - Functions/fractals
    - VSCode/Debugging
    - PythoShop
- Today going to talk about functions
- Math vs CS
    - Lots of overlap
        - functions
        - variables
        - boolean logic
    - CS stole a lot of these concepts
    - Today going to talk about functions
- Functions in math
    - Take input(s) and produces output
    - Function notation: `f(x) = x / 2`
        - `f(4)`
        - `f(f(8))`
        - CS can do better names -> halve(x)
    - Common math functions
        - sqrt
        - absolute value
        - addition
    - What is order of operations?
        - Ordering of functions when things on a single line
        - How to write `4 * 5 + 6 / 3`
            - `add(mul(4, 5), div(6, 3))`
- Start classwork
    - Schoology assessment first
        - Goal is to set you up to see similarities between math and Python
    - Grok after
        - Pay particular attention to how `return` works
        - What does it mean when there's no `return`, vs `return`, vs `return x`?

### Homework

- Finish Grok Lesson 8.2
- Schoology assessment
