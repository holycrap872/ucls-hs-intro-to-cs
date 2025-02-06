def func(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        prev_1 = func(x - 1)
        prev_2 = func(x - 2)
        return prev_1 + prev_2


print(func(15))
