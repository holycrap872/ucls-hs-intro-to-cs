# Introduction to Python: Practice Test

0. What are the "data types" of each of the following lines of code:

    - `chr()`
    - `"hey there"`
    - `"6.0"`
    - `"6"`
    - `elif`

1. What is the result of the following operations/functions:

    - `"5" + "1"`
    - `"5" + 1`
    - `5 * "1"`
    - `int(5 * "1") + 1`
    - `"AbbA".upper()`
    - `"AbbA".lower()`
    - `"AbbA".isupper()`
    - `ord("a")`
    - `chr(97)`

2. What would each of the following lines of code print out?

    - `name = "Person"; print(f"Hi name")`
    - `name = "Person"; print(f"Hi {name}")`
    - `name = "Person"; print("Hi {name}")`
    - `name = "Person"; print f"{Hi name}"`

3. Explain the difference between `2`, `2.0`, and `"2.0"` and why knowing they're
    different is important.

4. Identify the errors that occur on each line of the following program:

    ```python
    x == input("Enter a number: ")
    if x + 1 == 0:
        print(It's negative one)
    elif:
        print('It's two!')
        else:
        write("Honestly not sure")
    ```

5. Which of the following inputs would result in "a", "c", then "f" being printed out:

    ```python
    num_1 = int(input("First number: "))
    num_2 = int(input("Second number: "))

    if num_1 < 10:
        print("a")
    else:
        print("b")

    if num_2 == 5:
        print("c")
    else:
        print("d")

    if num_1 + num_2 == 11:
        print("e")
    elif num_1 + num_2 == 12:
        print("f")
    else:
        print("g")
    ```

6. Write a program that checks the strength of a user's password. The rules for
    the strength of a password are:

    - Passwords that are at least 10 characters long AND are all uppercase letters should should have "Strong Password" printed
    - All other passwords should have "Weak Password" printed

    Your program will need to use the `.isupper() ` and the `len()` functions.
    Begin your program with the line: `password = input("Enter your password: ")`

7. Create a program that asks the user for three numbers and prints the largest.

8. Write a program that asks the user for a work and then prints out every
    letter in the word with an exclamation point with a `!` after it. For
    example, if the user inputs `"hi!"`, the program will print out:

    ```
    h!
    i!
    !!
    ```

    Begin your program with the line: `word = input("Enter your word: ")`

9. Manually trace through the following program. What does it print out?
    ```python
    acc = ""
    for i in range(8):
        acc = str(i) + acc
    print(acc)
    ```

10. In 2-3 sentences, explain a real-life situation that could be described with
    an accumulator pattern.

11. Create a program that asks the user for a single number and then finds the
    sum of all of the numbers that are **less than or equal to** that number. For
    example, if the user says 1, the program should say 1. If the user says 2,
    the program should say 3. If the user says 5, the program should say 15.

    Hint: You should have an _accumulator variable_ that starts at 0.

# Answers
# On
# Next
# Page
# ...
# ...
# ...
# ...
# ...

0. What are the "data types" of each of the following lines of code:

    - `chr()` -> function
    - `"hey there"` -> string
    - `"6.0"` -> float
    - `"6"` -> int
    - `elif` -> control statement

1. What is the result of the following operations/functions:

    - `chr()` -> function
    - `"hey there"` -> string
    - `"6.0"` -> float
    - `"6"` -> int
    - `elif` -> control statement

2. What would each of the following lines of code print out?

    - `name = "Person"; print(f"Hi name")` -> "Hi name"
    - `name = "Person"; print(f"Hi {name}")` -> "Hi Person"
    - `name = "Person"; print("Hi {name}")` -> "Hi {name}"
    - `name = "Person"; print f"{Hi name}"` -> SyntaxError


3. Explain the difference between `2`, `2.0`, and `"2.0"` and why knowing they're
    different is important.
   
    The difference between these three things are their types. `2` is an integer,
    `2.0` is a float, and `"2.0"` is a string. Knowing their type allows you to
    determine which operations you can do on them. For example, the `+` operation
    acts differently on strings and integers.

4. Identify the errors that occur on each line of the following program:

    ```python
    x == input("Enter a number: ")
    if x + 1 == 0:
        print(It's negative one)
    elif:
        print('It's two!')
        else:
        write("Honestly not sure")
    ```

    1. Should be `=` instead of `==`
    2. Adding a number to a string
    3. Missing quotations marks
    4. Missing "condition" after the `elif`
    5. Wrong indentation
    6. Should be `print` instead of `write`

5. Which of the following inputs would result in "a", "c", then "f" being printed out:

    ```python
    num_1 = int(input("First number: "))
    num_2 = int(input("Second number: "))

    if num_1 < 10:
        print("a")
    else:
        print("b")

    if num_2 == 5:
        print("c")
    else:
        print("d")

    if num_1 + num_2 == 11:
        print("e")
    elif num_1 + num_2 == 12:
        print("f")
    else:
        print("g")
    ```

    - Input 1: 7, Input 2: 5

6. Write a program that checks the strength of a user's password. The rules for
    the strength of a password are:

    - Passwords that are at least 10 characters long AND are all uppercase letters should should have "Strong Password" printed
    - All other passwords should have "Weak Password" printed

    Your program will need to use the `.isupper() ` and the `len()` functions.
    Begin your program with the line: `password = input("Enter your password: ")`

    ```python
    password = input("Enter your password: ")
    if len(password) < 10:
        print("Weak Password")
    elif password.isupper():
        print("Strong Password")
    else:
        print("Weak password")
    ```

7. Create a program that asks the user for three numbers and prints the largest.

    ```python
    num_1_str = input("Enter your first number: ")
    num_2_str = input("Enter your second number: ")
    num_3_str = input("Enter your third number: ")
    num_1 = int(num_1_str)
    num_2 = int(num_2_str)
    num_3 = int(num_3_str)

    if num_1 > num_2:
        if num_1 > num_3:
            print(num_1)
        else:
            print(num_3)
    else:
        if num_2 > num_3:
            print(num_2)
        else:
            print(num_3)
    ```

8. Write a program that asks the user for a work and then prints out every
    letter in the word with an exclamation point with a `!` after it. For
    example, if the user inputs `"hi!"`, the program will print out:

   ```
    h!
    i!
    !!
    ```

    Begin your program with the line: `word = input("Enter your word: ")`

    ```python
    word = input("Enter your word: ")
    for letter in word:
        print(f"{letter}!")
    ```

9. Manually trace through the following program. What does it print out?
    ```python
    acc = ""
    for i in range(8):
        acc = str(i) + acc
    print(acc)
    ```

    - `"76543210"`

10. In 2-3 sentences, explain a real-life situation that could be described with
   an accumulator pattern.

   When reviewing monthly bank statements, you keep a total (accumulator
   variable) and go through each transaction. If it's a deposit, you add to your
   total; if it's a withdrawal, you subtract (accumulation steps with selection
   conditions). The final balance (accumulation result) tells you how much money
   you have.

11. Create a program that asks the user for a single number and then finds the
    sum of all of the numbers that are **less than or equal to** that number. For
    example, if the user says 1, the program should say 1. If the user says 2,
    the program should say 3. If the user says 5, the program should say 15.

    Hint: You should have an _accumulator variable_ that starts at 0.

    ```python
    num = int(input("Enter a number: "))
    acc = 0
    for i in range(num + 1):
        acc = acc + i
    print(acc)
    ```
