#!/usr/bin/env python3
import argparse
import typing

import numpy as np
from PIL import Image


def image_to_emoji(image_path: str, max_size=30) -> typing.Tuple[str, str]:
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.width / img.height
    if aspect_ratio > 1:  # Image is wide
        img = img.resize((max_size, int(max_size / aspect_ratio)))
    else:  # Image is tall or square
        img = img.resize((int(max_size * aspect_ratio), max_size))

    # Convert to numpy array
    img_array = np.array(img)

    # Define the emoji colors (RGB)
    colors = {
        (255, 0, 0): ("🟥", "100"),  # Red
        (0, 255, 0): ("🟩", "010"),  # Green
        (0, 0, 255): ("🟦", "001"),  # Blue
        (255, 255, 0): ("🟨", "110"),  # Yellow
        (255, 255, 255): ("⬜", "111"),  # White
        (255, 0, 255): ("🟪", "101"),  # Magenta
        (0, 0, 0): ("⬛", "000"),  # Black
        (0, 255, 255): ("🟦", "011"),  # Cyan (represented with a heart)
    }

    # Function to find the nearest color
    def find_nearest_color(rgb):
        return min(colors.keys(), key=lambda color: sum((s - q) ** 2 for s, q in zip(color, rgb)))

    # Create emoji representation
    emoji_representation = ""
    text_representation = ""
    for row in img_array:
        for pixel in row:
            nearest_color = find_nearest_color(pixel[:3])
            emoji_representation += colors[nearest_color][0]
            text_representation += colors[nearest_color][1]

        emoji_representation += "\n"
        text_representation += "222"

    return emoji_representation, text_representation


# Replace 'your_image_path.png' with the path to your image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to file", type=str, required=True)
    parser.add_argument("-s", "--size", help="Max size", type=int, required=True)
    args = parser.parse_args()

    emoji_art, text_rep = image_to_emoji(args.path, max_size=args.size)
    print(emoji_art)
    print()
    print(text_rep)
