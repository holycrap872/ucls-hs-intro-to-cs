## Essential Questions

- What is an IDE?
- How can we visualize loops and recursion?

## Lesson Plan

### Setup

- `Turbozzle One Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1aCPLTZ5ZrnDYkBXXE87BTv3F9QBSN4nd8OhKO1DcTCc
- Turbozzle "Skeleton" loaded up in Schoology
    - https://github.com/eric-rizzi/ucls-turbozzle
        - `for_students` branch
    - Remove extra junk
        - `image` folder (used for "main" page in github)
        - `find . -name "__pycache__" -exec rm -r {} \;`
        - `find . -name ".DS_STORE" -exec rm -r {} \;`
        - `find . -name "*pytest_cache*" -exec rm -r {} \;`
- Schoology Assessment
    - TODO

### Actual Lesson

- Opening Problem
    - `opening_problem.py`
    - Simulating a game of telephone
- Review
    - Functions
    - Robozzle
    - vscode
- Robozzle
    - Play https://alexanderson1993.github.io/robozzle-react/?level=16166
    - How like abstraction?
    - Point out key parts of Robozzle
        - Limited spaces leads to code folding
        - Limited number of options for spaceship
- Turbozzle
    - Explain rules
        - Need to get to all of the yellow w/o hitting black
        - Once get all yellow, the turtle spins in celebration
    - Do walkthrough
        - Different levels/files
        - 50 pixel increments
        - `forward()` requires no arguments
        - `left()` and `right()` require arguments
    - Show students how to do a split screen
        - Code on left, picture on right
    - How is this similar to/different from Robozzle?
        - Similar because controlling motion with functions
        - Different because more powerful (have variables)
    - Show final level (tree)
        - Example of recursion
        - Wouldn't be possible in Robozzle
- Go!
    - Work with a partner, but each person needs to submit their own worksheet
    - LOTS of absences at this point in the year... makes it hard

### Homework

- TIL entry on what `import` means
