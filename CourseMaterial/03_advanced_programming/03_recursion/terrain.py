import pygame
import random

def diamond_square(size, roughness):
    # Initialize the 2D array with zeros
    arr = [[0 for _ in range(size + 1)] for _ in range(size + 1)]

    # Initial corner values
    arr[0][0] = arr[0][size] = arr[size][0] = arr[size][size] = size // 2

    step = size // 2
    while step > 0:
        # Diamond step
        for x in range(0, size, step * 2):
            for y in range(0, size, step * 2):
                avg = (arr[x][y] + arr[x + step * 2][y] + arr[x][y + step * 2] + arr[x + step * 2][y + step * 2]) / 4
                arr[x + step][y + step] = avg + random.uniform(-step, step) * roughness

        # Square step
        for x in range(0, size + 1, step):
            shift = step if x % (step * 2) == 0 else 0
            for y in range(shift, size + 1, step * 2):
                total = 0
                count = 0
                if x >= step:
                    total += arr[x - step][y]
                    count += 1
                if x + step <= size:
                    total += arr[x + step][y]
                    count += 1
                if y >= step:
                    total += arr[x][y - step]
                    count += 1
                if y + step <= size:
                    total += arr[x][y + step]
                    count += 1

                arr[x][y] = total / count + random.uniform(-step, step) * roughness

        step //= 2
        roughness /= 2

    return arr

def render_landscape(screen, landscape):
    sky_color = (135, 206, 235)  # Blue sky
    screen.fill(sky_color)

    max_height = max(max(row) for row in landscape)
    height_factor = 255 / max_height  # Factor to scale heights to color intensity

    for y in range(len(landscape)):
        # Generate points for the mountain polygon
        points = [(0, screen.get_height())]  # Start at bottom left
        for x, height in enumerate(landscape[y]):
            # Convert height to a vertical position
            height = int(height * height_factor)
            mod_height = screen.get_height() - (height + 350)
            points.append((x, mod_height))
        points.append((screen.get_width(), screen.get_height()))  # End at bottom right

        # Draw the mountain polygon
        color = (0, 10 + (y // 5), 0)
        pygame.draw.polygon(screen, color, points)

def main():
    pygame.init()

    size = 1025  # Must be 2^n + 1 for the algorithm
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Mountain Landscape")

    landscape = diamond_square(size - 1, roughness=100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_landscape(screen, landscape)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

