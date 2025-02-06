1. What is the definition of recursion?
    - When a concept or process depends on a simpler version of itself
    - When a set of input(s) produce a single output
    - When two Python functions are called from a third, higher-level function
    - When f(x) has a series of associated rules
2. Label each of the parts of the following recursive function
    - Base case
    - Recursive step
    - Function call
    - Function body
3. What is the result of running the following code:
    ```python
    def f(x, y):
        if x == y:
            print("done")
        else:
            print(x)
            f(x + 1)
    f(0, 10)
    ```
    - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, done
    - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, done
    - 9, 8, 7, 6, 5, 3, 2, 1, 0, done
    - 10, 9, 8, 7, 6, 5, 3, 2, 1, 0, done
4. What is the result of running the following code:
    ```python
    def f(x, y):
        if x == y:
            print("done")
        else:
            print(x)
            f(y - 1)
    f(0, 10)
    ```
    - 1, 2, 3, 4, 5, 6, 7, 8, 9, done
    - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, done
    - 9, 8, 7, 6, 5, 4, 3, 2, 1, done
    - 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, done
5. What is the result of running the following code:
    ```python
    def f(x, y, z):
        if x == z:
            print("done")
        else: 
            print(x)
            f(x + y, y, z)
    f(4, 3, 15)
    ```
    - 4, 7, 10, 13, done
    - 4, 6, 8, 10, 12, 14, done
    - 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, done
    - 4, 3, 15, done
6. What is the result of running the following code:
    ```python
    def f(w):
        print(w[0])
        print(w[2])
        print(w[-1])
        print(w[-3])
        
    word = "hithere"
    f(word)
    ```
7. What is the result of running the following code:
    ```python
    def g(s):
        for i in range(len(s) - 1):
            c = s[i]
            print(c)
    g("hithere")
    ```
    - h, i, t, h, e, r
    - h, i, t, h, e, r, e
    - h, i, t, h, e
    - i, t, h, e, r
8. What is the result of running the following code:
    ```python
    def g(s):
    for i in range(len(s) - 1):
        c1 = s[i]
        c2 = s[i + 1]
        print(f"{c1}, {c2}")
    print("done")

    g("hello")
    ```
    - h-e, e-l, l-l, l-o, done
    - h-h, e-e, l-l, l-l, o-o, done
    - h-, e-, l-, l-, o-, done
    ```
9. Throwback: Use the RGB chart below to match the colors with their hexadecimal representation:
    - 0xFFFFFF
    - 0x000000
    - 0xFF0000
    - 0x0000FF
    - 0xFF00FF
    - 0xFFFF00
