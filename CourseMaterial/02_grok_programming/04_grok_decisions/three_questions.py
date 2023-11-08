#!/usr/bin/env python3

msft_product = input("Is it a Microsoft product? ")
if msft_product == "y":
    is_geometry = input("Is it associated with geometry? ")
    if is_geometry == "y":
        knifes_edge = input("Is it the sharp part of a knife? ")
        if knifes_edge == "y":
            print("Your word is 'edge'!")
        else:
            print("Your word is 'surface'!")
    else:
        in_books = input("Is it in books? ")
        if in_books == "y":
            print("Your word is 'word'!")
        else:
            print("Your word is 'bing'!")
else:
    is_sound = input("Is it word that describes the sounds animals make? ")
    if is_sound == "y":
        is_pig = input("Do pigs make this noise? ")
        if is_pig == "y":
            print("Your word is 'squeal'!")
        else:
            print("Your word is 'sing'!")
    else:
        in_quiddich = input("Is it used in quiddich? ")
        if in_quiddich == "y":
            print("Your word is 'snitch'!")
        else:
            print("Your word is 'rat'!")
