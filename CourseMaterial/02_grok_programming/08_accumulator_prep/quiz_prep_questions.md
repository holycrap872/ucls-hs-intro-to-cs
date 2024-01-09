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

5. Given the starter code below, create a program to print out the price of a movie ticket based on age:
    - Tickets are $12 for adults (ages 13 to 64).
    - $7 for children (ages 3 to 12) and seniors (65 and older).
    - Free for toddlers (below 3 years).

    ```python
    age = int(input("Enter your age: "))
    ```
# Answers

1. Code:

```python
input_str = input("What is your string? ")
for c in input_str:
  print(c)
```

2. The input is a string and needs to be changed to an integer. It should be `num_str = int(input("Enter a number: "))`

3. Code:

```python
num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))

for i in range(num_1 + 1, num_2):
  print(i)
```

4. The range function allows you to iterate over a given series of numbers. This is useful because it allows you to find and exploit patterns via loops, leading to shorter, more flexible code.

5. Code:

```python
age = int(input("Enter your age: "))
if 13 <= age <= 64:
  print("You owe $12")
elif age < 3:
  print("You own $0")
else:
  print("You owe $7")
```
