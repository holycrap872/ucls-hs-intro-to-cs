# Grok Lesson 5 and Functions Practice Problems

1. Create a function that takes three integers as inputs and returns their sum. Then, call the function with the numbers 1, 6, 8 and print the result.

2. What does the following program print out?
    ```python
    word = "cow"
    acc = ""
    for c in word:
      acc = c + acc + acc

    print(acc)
    ```

3. Create a program that asks the user for a starting and ending integer, then uses a loop to print out all of the numbers _between_ (and including) those numbers.

4. Create a program that uses a loop to add all of the numbers between 1 and 10 and then prints out the result. Hint: you need to use an accumulator variable that is set to 0 _outside_ the loop.

5. Identify the following parts of the given code:
    ```python
    def say_hi(name):
        return "Hello there " + name

    greeting = say_hi("Carl")
    ```
    - The word that denotes a function is being created:
    - The name of the function:
    - The number of inputs to the function and their types:
    - What the function returns and its type:
    - The function call:

6. Explain why functions are so important in Computer Science.

# Answers

1. Code:

```python
def add(x, y, z):
  return x + y + z

ans = add(1, 6, 8)
print(ans)
```

2. The program prints out the string `"woccocc"`

3. Code:

```python
num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))

for i in range(num_1, num_2 + 1):
  print(i)
```

4. Code:

```python
acc = 0
for i in range(1, 11):
  acc = acc + i
print(acc)
```

5. Pieces of the function:
    - The word that denotes a function is being created: `def`
    - The name of the function: `say_hi`
    - The number of inputs to the function and their types: One and it's an integer
    - What the function returns and its type: It returns a string that says "hi NAME"
    - The function call: `say_hi("Carl")`

6. Functions are important for two reasons. First, they help minimize the amount of code in a program; wherever  there is repeated code, it can be put inside a function so it only needs to be written once. Second, it allows people to work together. Once person can work on the code _inside_ the function and the other can just assume the function works and call it. This allows people to split work effectively.