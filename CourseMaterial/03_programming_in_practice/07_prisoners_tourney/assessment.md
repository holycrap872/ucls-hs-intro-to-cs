0. Match the following operations with their results:
    - `len([1, 2, 4, 8])`
    - `len("hello")`
    - `x = "1234"; x[0]`
    - `x = [1, 2, 4, 8]; x[0]`
    - `x = [1, 2, 4, 8]; x[0] + x[-1]`
    - `x = "1248"; x[0] + x[-1]`
1. What is the result of the following bit of code:
    ```python
    l = [1, 2]
    l.append(3)
    add = l[0] + l[-1]
    print(add)
    ```
    - 4
    - 13
    - 3
    - 1
    - -1
2. What is the result of the following bit of code:
    ```python
    l = []
    l.append(4)
    l.append(5)
    l.append(l[0])
    l.append(l[1])
    print(l)
    ```
    - [4, 5, 4, 5]
    - [4, 5, 4, 4]
    - [4, 5, 5, 5]
    - [4, 5, 5, 4]
3. What is the result of the following bit of code:
    ```python
    l = []
    for i in range(4):
        l.append(i + 1)
    print(l)
    ```
    - [1, 2, 3, 4]
    - [0, 1, 2, 3]
    - [1, 3, 5, 7]
    - [2, 3, 5, 8]
4. What is the result of the following bit of code:
    ```python
    l = [1, 1]
    for i in range(4):
        x = l[-1]
        y = l[-2]
        l.append(x + y)
    print(l)
    ```
    - [1, 1, 2, 3, 5, 8]
    - [0, 1, 1, 2, 2, 3]
    - [1, 2, 4, 8, 16, 32]
    - [1, 2, 3, 4, 5, 6]
5. What is the result of the following bit of code:
    ```python
    l = [1, 2, 3, 4]
    new_l = []
    for elem in l:
        new_l.append(elem * 3)
    print(new_l)
    ```
    - [3, 6, 9, 12]
    - [1, 3, 6, 9]
    - [4, 5, 6, 7]
    - [3, 9, 27, 81]
