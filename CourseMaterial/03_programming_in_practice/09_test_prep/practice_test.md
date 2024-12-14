# Programming in Practice: Practice Test

0. Manually trace through the following program. What does it print out?
    ```python
    l = [1, 1]
    for i in range(0, 8, 2):
        x = l[-1]
        y = l[-2]
        l.append(x + y)
    print(l)
    ```

1. Create a program that asks the user for three space-separated numbers on a
   single line and prints the largest.

2. Create a program that asks the user for their name, puts every individual
   character in their name into a list, and then prints out the list.

3. Create an equivalent `for` loop for the following bit of code:

    ```python
    i = 3
    while i < 9:
        print(i)
        print(i - 1)
        i = i + 2
    ```

4. Create a function named `list_adder` that takes a list of integers and
   returns the sum of all of those integers.

5. Identify the following parts of the given code:

    ```python
    def subtract_two(val):
        return val - 2

    result = subtract_2(10)
    ```
    - The word that denotes a function is being created:
    - The name of the function:
    - The number of inputs to the function and their types:
    - What the function returns and its type:
    - The function call:

6. In 2-3 sentences, explain a real-life situation that could be described with
   a `for` and a list.

# Answers
# On
# Next
# Page
# ...
# ...
# ...
# ...
# ...
# ...
# ...

0. `[1, 1, 2, 3, 5, 8]`

1. Code:

    ```python
    nums_str = input("Enter your three numbers (with spaces in between): ")
    nums_list = nums_str.split()
    num_1 = int(nums_list[0])
    num_2 = int(nums_list[1])
    num_3 = int(nums_list[2])

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

2. Code:

    ```python
    name_str = input("What is your name? ")

    name_list = []
    for char in name_str:
    name_list.append(char)
    
    print(name_list)
    ```

3. Code:

    ```python
    for i in range(3, 9, 2):
        print(i)
        print(i - 1)
    ```

4. Code

    ```python
    def list_adder(l):
        sum = 0
        for item in l:
            sum = sum + item

        return sum
    ```

5. Pieces of the function:
    - The word that denotes a function is being created: `def`
    - The name of the function: `subtract_two`
    - The number of inputs to the function and their types: One and it's an integer
    - What the function returns and its type: It returns a integer that is two less than the input
    - The function call: `subtract_2(10)`

6. A real-life example of using a for loop and a list is organizing a birthday
    party invitation list. You have a list of friends' names and use a for loop
    to automatically send an invitation email to each person on the list. This
    method efficiently ensures that no one is missed and everyone receives a
    personalized invite.
