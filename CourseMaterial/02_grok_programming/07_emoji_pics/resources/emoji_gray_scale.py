from PIL import Image
import numpy as np

def image_to_emoji_grayscale(image_path, max_size=26):
    # Load the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale

    # Resize the image
    aspect_ratio = img.width / img.height
    if aspect_ratio > 1: # Image is wide
        img = img.resize((max_size, int(max_size / aspect_ratio)))
    else: # Image is tall or square
        img = img.resize((int(max_size * aspect_ratio), max_size))

    # Convert to numpy array
    img_array = np.array(img)

    # Map the grayscale values to two-bit (four-level) grayscale
    img_array //= 64  # Integer division by 64 to get values in [0, 3]

    # Define the grayscale emojis
    grayscale_emojis = {
        3: "⬜",  # White
        2: "🔲",  # Light gray
        1: "🔳",  # Dark gray
        0: "⬛",  # Black
    }

    # Create emoji representation
    emoji_representation = ""
    for row in img_array:
        for value in row:
            emoji_representation += grayscale_emojis[value]
        emoji_representation += "\n"

    return emoji_representation

# Replace 'your_image_path.png' with the path to your image
emoji_art_grayscale = image_to_emoji_grayscale('/Users/ericrizzi/Desktop/mario.png')
print(emoji_art_grayscale)

