from PIL import Image
import numpy as np

def image_to_emoji(image_path, max_size=26):
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.width / img.height
    if aspect_ratio > 1: # Image is wide
        img = img.resize((max_size, int(max_size / aspect_ratio)))
    else: # Image is tall or square
        img = img.resize((int(max_size * aspect_ratio), max_size))

    # Convert to numpy array
    img_array = np.array(img)

    # Define the emoji colors (RGB)
    colors = {
        (255, 0, 0): "🟥",       # Red
        (0, 255, 0): "🟩",       # Green
        (0, 0, 255): "🟦",       # Blue
        (255, 255, 0): "🟨",     # Yellow
        (255, 255, 255): "⬜",   # White
        (255, 0, 255): "🟪",     # Magenta
        (0, 0, 0): "⬛",         # Black
        (0, 255, 255): "💙"      # Cyan (represented with a heart)
    }

    # Function to find the nearest color
    def find_nearest_color(rgb):
        return min(colors.keys(), key=lambda color: sum((s - q) ** 2 for s, q in zip(color, rgb)))

    # Create emoji representation
    emoji_representation = ""
    for row in img_array:
        for pixel in row:
            nearest_color = find_nearest_color(pixel[:3])
            emoji_representation += colors[nearest_color]
        emoji_representation += "\n"

    return emoji_representation

# Replace 'your_image_path.png' with the path to your image
emoji_art = image_to_emoji('/Users/ericrizzi/Desktop/mario.png')
print(emoji_art)

