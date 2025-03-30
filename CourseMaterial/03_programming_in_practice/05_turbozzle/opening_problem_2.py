#!/usr/bin/env python3
def do_something(word):
    x = word[0]
    y = word[1]
    z = word[2]
    return f"{x}{y}-{z}{y}"


if __name__ == "__main__":
    ret = do_something("tad")
    print(ret)
