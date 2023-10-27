import random

import pygame


def run_game():
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    width = 640
    height = 480
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # The game loop starts here.
    keep_going = True

    red = 0
    blue = 0xFF
    green = 0xFF

    while keep_going:
        # User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        # "Move"
        change = random.choice(["RED", "GREEN", "BLUE"])
        direction = random.choice([1, -1])
        if change == "RED":
            red += direction * 20
            if red > 0xFF:
                red = 0xFF
            if red < 0:
                red = 0
        elif change == "GREEN":
            green += direction * 20
            if green > 0xFF:
                green = 0xFF
            if green < 0:
                green = 0
        else:
            blue += direction * 20
            if blue > 0xFF:
                blue = 0xFF
            if blue < 0:
                blue = 0

        # Draw picture and update display
        print("Red", red, "Green", green, "Blue", blue)
        screen.fill(pygame.color.Color(red, green, blue))

        pygame.display.flip()
        clock.tick(20)  # limits FPS to 60

    # The game loop ends here.
    pygame.quit()


# Main hook
if __name__ == "__main__":
    run_game()
