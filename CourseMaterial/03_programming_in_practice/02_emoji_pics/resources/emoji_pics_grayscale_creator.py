#!/usr/bin/env python3
import argparse
import typing

import numpy as np
from PIL import Image


def image_to_emoji_grayscale(image_path: str, max_size=26) -> typing.Tuple[str, str]:
    # Load the image
    img = Image.open(image_path).convert("L")  # Convert to grayscale

    # Resize the image
    aspect_ratio = img.width / img.height
    if aspect_ratio > 1:  # Image is wide
        img = img.resize((max_size, int(max_size / aspect_ratio)))
    else:  # Image is tall or square
        img = img.resize((int(max_size * aspect_ratio), max_size))

    # Convert to numpy array
    img_array = np.array(img)

    # Map the grayscale values to two-bit (four-level) grayscale
    img_array //= 64  # Integer division by 64 to get values in [0, 3]

    # Define the grayscale emojis
    grayscale_emojis = {
        3: ("⬜", "11"),  # White
        2: ("🔲", "10"),  # Light gray
        1: ("🔳", "01"),  # Dark gray
        0: ("⬛", "00"),  # Black
    }

    # Create emoji representation
    emoji_representation = ""
    text_representation = ""
    for row in img_array:
        for value in row:
            emoji_representation += grayscale_emojis[value][0]
            text_representation += grayscale_emojis[value][1]

        emoji_representation += "\n"
        text_representation += "22"

    return emoji_representation, text_representation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to file", type=str, required=True)
    parser.add_argument("-s", "--size", help="Max size", type=int, required=True)
    args = parser.parse_args()

    emoji_art, text_rep = image_to_emoji_grayscale(args.path, max_size=args.size)
    print(emoji_art)
    print()
    print(text_rep)
