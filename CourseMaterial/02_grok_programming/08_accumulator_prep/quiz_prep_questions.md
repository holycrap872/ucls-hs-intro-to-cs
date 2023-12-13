# Grok Lesson 1 - 5.2 Practice Problems

1. Create a program that asks the user for a string and then (using a loop) prints out each character in the string on its own line.

2. What is the problem with the following bit of code that attempts to print out every number between 0 and the number a user enters:
    ```python
    num_str = input("Enter a number: ")
    for i in range(0, num_str):
        print(i)
    ```

3. Create a program that asks the user for a starting and ending integer, then uses a loop to print out all of the numbers _between_ (not including) those numbers.

4. In 2-3 sentences, explain what the `range()` function does and why it is useful?

5. Given the starter code below, create a program to determine the price of a movie ticket based on age:
    - Tickets are $12 for adults (ages 13 to 64).
    - $7 for children (ages 3 to 12) and seniors (65 and older).
    - Free for toddlers (below 3 years).

    ```python
    age = int(input("Enter your age: "))
    ```
