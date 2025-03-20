# Grok Lesson 6 Practice Problems

1. Manually trace through the following program. What does it print out?
    ```python
    acc_list = [3]
    for i in range(4):
        tmp = acc_list[i] * 3
        acc_list.append(tmp)
            
    print(acc_list)
    ```

2. Create a program that asks the user for three, space-separated numbers and
   then returns all three numbers multiplied together.

3. Given the list `l = [6, 10, 3, 2, 4]`, what would `nl = l[1:]` do?

4. What would the following bit of code print out?
    ```python
    l = [0, 0]
    l[0] = 5
    l[1] = l[0] + l[1] + 2
    print(l)
    ```

5. Create a program that asks the user for their name, puts every individual
   character in their name into a list, and then prints out the list.

6. List two ways that lists are similar to strings.

# Answers
# On
# Next
# Page

1. The program prints out the list `[3, 9, 27, 81, 243]`.

2. Code:

```python
number_str_input = input("Enter three space-separated integers: ")
number_str_list = number_str_input.split()

acc = 1
for number_str in number_str_list:
  acc = acc * int(number_str)
  
print(acc)
```


3. It would create a new sub-list that was the same as the original list BUT
   with the first number missing/sliced away. (e.g., `nl would be [10, 3, 2, 4]`)

4. The program prints out the list `[5, 7]`.

5. Code:

```python
name = input("What is your name? ")
l = []
for char in name:
    l.append(char)
print(l)
```

6. Lists and strings are similar in that they:
    - You can iterate through them
    - You can use an index to access them
    - They are composed of individual elements
    - They can be empty