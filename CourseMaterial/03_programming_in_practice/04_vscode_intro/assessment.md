0. What is the definition of abstraction in Computer Science?
    - Hiding unnecessary details
    - Adding useful information
    - Thinking about details
    - Working on two things at once
1. How do people use abstraction when they communicate?
    - They talk at a high level and explain details when needed
    - They explain all of the details all at once
    - They think at a high level and explain everything at a low level
    - They explain things like ideas but omit things like actions
2. Which of the following is the most abstract recipe for making an omelette?
    - Throw some beaten eggs in a hot pan
    - Get three eggs, crack and beat them, put them in a heated pan, wait until the eggs harden
    - Get some eggs, beat them, pour them into a hot pan and wait for the bottom to brown
    - Pick up an egg by holding your hand over the shell then flexing you arm slightly. Then, lower the egg quickly on the edge of bowl ...
3. Label each of the parts of the function that are pointed to in the picture below:
    - Name of function
    - Input(s) to function
    - Creates function
    - Function call
    - Output of function
4. How is creating a good function name an example of abstraction?
    - By describing the functions behavior (what), you prevent the caller from having to think about the details (how)
    - By explaining times that the function should be called (when), you avoid having the caller put it in the wrong place (where)
    - By creating the function near the function call (where), you give a hint at how often the function should be called (when)
    - By listing the instructions inside the function (how), you let the caller know the purpose of calling the function (why)
5. When run, the program below would output:
    ```python
    def do_something_0(string, letter):
        acc = ""
        for c in string:
            if c != letter:
                acc = acc + c
        return acc


    if __name__ == "__main__":
        ret = do_something_0("encyclopedia", "c")
        ret = do_something_0(ret, "e")
        print(ret)
    ```
    - "nylopdia"
    - "ecce"
    - "cececececece"
    - "cneyelopcdia"
    - "EnCyClOpEdIa"
6. A better name for the function above than `do_something_0` is:
    - remove_letter
    - count_letter
    - add_letters
    - return_string_op
7. Which of the following inputs would result in "a", "c", then "f" being printed out:
    ```python
    def do_something_1(x, y):
        if x < 6:
            print("a")
        else:
            print("b")

        if x > 4:
            print("c")
        else:
            print("d")

        if x + y == 11:
            print("e")
        elif x + y == 12:
            print("f")
        else:
            print("g")

    if __name__ == "__main__":
        num_1 = int(input("First number: "))
        num_2 = int(input("Second number: "))
        do_something_1(num_1, num_2)
    ```
    - Input 1: 5, Input 2: 7
    - Input 1: 5, Input 2: 6
    - Input 1: 4, input 2: 8
    - Input 1: 4.  Input 2: 6
8. Flashback: What is the number 0b1101 converted to decimal?
    - 0d13
    - 0d16
    - 0d9
    - 0d7
