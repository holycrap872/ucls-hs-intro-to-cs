1. What is the definition of a function
    - Something that takes input(s) and produces an output
    - Something that takes a single input and produces multiple outputs
    - Something that produces a constant output unrelated to input(s)
    - Something that takes a set of input(s) and combines them
2. In math, the sqrt symbol can be considered a function. Why?
    - Because it takes input(s) and produces a single output
    - Because it is an exponent which is the E in PEMDAS
    - Because it is required to take one or more inputs when "called"
    - Because it has higher precedence than the + or - symbol
3. What is the definition of recursion?
    - When a concept or process depends on a simpler version of itself
    - When a set of input(s) produce a single output
    - When two Python functions are called from a third, higher-level function
    - When f(x) has a series of associated rules
4. What makes a recursive function different from a regular function?
    - The function has to call itself
    - The function must have exactly one input
    - The function needs to use a for loop
    - The function requires multiple print statements
5. Why does every recursive function need a base case?
    - To prevent infinite recursion
    - To ensure the function returns something
    - To make the code run faster
    - To follow Python syntax rules
6. Label each of the parts of the recursive function that are pointed to in the picture below:
    - Name of function
    - Function call
    - Recursive step
    - Base case
    - Body of function
7. What is wrong with the following recursive function?
    ```python
    def count_down(n):
        print(n)
        count_down(n-1)
    
    count_down(10)
    ```
    - There is no base case
    - The function name is invalid
    - The input is too large
    - The body of the function is too short
8. What is the result of running the following code:
    ```python
    def add_letter(x):
        if len(x) >= 5:
            print(x)
        else:
            add_letter(x + "a")

    add_letter("hi")
    ```
    - hiaaa
    - aaaaa
    - aaahi
    - aahia
