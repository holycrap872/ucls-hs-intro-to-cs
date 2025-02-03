def decrement(x):
    if x == 0:
        print("all done")
    else:
        print(x)
        decrement(x - 1)


decrement(2)
