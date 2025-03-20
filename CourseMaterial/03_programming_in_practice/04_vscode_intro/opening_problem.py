#!/usr/bin/env python3
def decode(string_1, string_2):
    if len(string_1) != len(string_2):
        return "Can't decode"

    acc = ""
    for i in range(len(string_1)):
        if string_1[i] == "1":
            acc = acc + string_2[i]

    return acc


if __name__ == "__main__":
    ret = decode("01101", "GLARB")
    print(ret)
