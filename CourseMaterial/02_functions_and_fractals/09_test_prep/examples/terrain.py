import random

import pygame


def diamond_square_helper(arr: list[list[float]], size: int, roughness: float) -> None:
    half = size // 2
    if half < 0.5:
        return

    # Diamond step
    for y in range(half, len(arr) - 1, size):
        for x in range(half, len(arr[0]) - 1, size):
            avg = (
                arr[y - half][x - half] + arr[y - half][x + half] + arr[y + half][x - half] + arr[y + half][x + half]
            ) / 4.0
            arr[y][x] = avg + random.uniform(-roughness, roughness)

    # Square step
    for y in range(0, len(arr), half):
        for x in range((y + half) % size, len(arr[0]), size):
            total = 0
            count = 0

            # Check each adjacent point
            if y >= half:  # Top
                total += arr[y - half][x]
                count += 1
            if y + half < len(arr):  # Bottom
                total += arr[y + half][x]
                count += 1
            if x >= half:  # Left
                total += arr[y][x - half]
                count += 1
            if x + half < len(arr[0]):  # Right
                total += arr[y][x + half]
                count += 1

            if count > 0:
                arr[y][x] = (total / count) + random.uniform(-roughness, roughness)

    diamond_square_helper(arr, size // 2, roughness / 2)


def diamond_square_recursive(size: int, roughness: float) -> list[list[float]]:
    arr = [[0.0 for _ in range(size)] for _ in range(size)]

    # Set higher values for top corners (0,0) and (0,size-1)
    arr[0][0] = arr[0][size - 1] = random.uniform(roughness / 2, roughness)
    # Set lower values for bottom corners
    arr[size - 1][0] = arr[size - 1][size - 1] = random.uniform(0, roughness / 3)

    diamond_square_helper(arr, size - 1, roughness)
    return arr


def diamond_square_iterative(size: int, roughness: int) -> list[list[float]]:
    # Initialize the 2D array with zeros
    arr = [[0.0 for _ in range(size + 1)] for _ in range(size + 1)]

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
        roughness //= 2

    return arr


def render_landscape(screen: pygame.Surface, landscape: list[list[float]]) -> None:
    sky_color = (135, 206, 235)  # Blue sky
    screen.fill(sky_color)

    max_height = max(max(row) for row in landscape)
    height_factor = 255 / max_height  # Factor to scale heights to color intensity

    for y in range(len(landscape)):
        # Generate points for the mountain polygon
        points = []
        points.append((0, screen.get_height()))  # Start at bottom left
        for x, height in enumerate(landscape[y]):
            # Convert height to a vertical position
            height = int(height * height_factor)
            mod_height = screen.get_height() - (height + 150)
            points.append((x, mod_height))
        points.append((screen.get_width(), screen.get_height()))  # End at bottom right

        # Draw the mountain polygon
        color = (0, 0 + (y // 3), 0)
        pygame.draw.polygon(screen, color, points)


def main():
    pygame.init()

    size = 513  # Must be 2^n + 1 for the algorithm
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Mountain Landscape")

    # landscape = diamond_square_iterative(size - 1, 100)  # Adjust roughness as desired
    landscape = diamond_square_recursive(size, 1000)  # Adjust roughness as desired

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
