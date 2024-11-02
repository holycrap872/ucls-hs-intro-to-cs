import random

import pygame


def collision(x1: int, y1: int, width1: int, height1: int, x2: int, y2: int, width2: int, height2: int) -> bool:
    left1 = x1
    right1 = x1 + width1
    top1 = y1
    bottom1 = y1 + height1
    left2 = x2
    right2 = x2 + width2
    top2 = y2
    bottom2 = y2 + height2

    if bottom1 < top2 or top1 > bottom2 or right1 < left2 or left1 > right2:
        return False
    else:
        return True


def run_game():
    ## Initialize the pygame submodules and set up the display window.

    pygame.init()

    width = 640
    height = 480
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # The game loop starts here.
    keep_going = True

    heli_x = 30
    heli_y = 200
    heli_yspeed = 0
    heli_size = 20
    heli_color = "Red"

    terrain = []

    # Pattern
    # (x, height, hole size)
    # height = random amount within a certain amount
    terrain.append([640, random.randint(0, 340), random.randint(100, 300)])

    while keep_going:
        # User Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            heli_yspeed = heli_yspeed - 0.1
            heli_color = "Red"
        else:
            heli_yspeed = heli_yspeed + 0.1
            heli_color = "Green"

        # Move
        for i in range(0, len(terrain)):
            terrain[i][0] = terrain[i][0] - 3

        heli_y = int(heli_y + heli_yspeed)

        # Check for collisions

        # If terrain can't be seen anymore
        if terrain[0][0] + 50 < 0:
            terrain.pop(0)

        # If need more terrain
        if terrain[len(terrain) - 1][0] + 50 < width:
            terrain.append([640, terrain[len(terrain) - 1][1] + random.randint(-30, 30), random.randint(100, 300)])

        # If terrain too high
        if terrain[len(terrain) - 1][1] < 0:
            terrain[len(terrain) - 1][1]

        # If terrain too low
        if terrain[len(terrain) - 1][1] + terrain[len(terrain) - 1][2] > 640:
            terrain[len(terrain) - 1][1] = 640 - terrain[len(terrain) - 1][2]

        # Collisions with  blocks
        x = 0
        while x < 3 and x < len(terrain):
            block_x = terrain[x][0]
            block_y = terrain[x][1]
            block_hole = terrain[x][2]

            if collision(heli_x, heli_y, heli_size, heli_size, block_x, 0, 51, block_y):
                print("hit1")
                # keep_going = False

            if collision(
                heli_x, heli_y, heli_size, heli_size, block_x, block_y + block_hole, 51, height - (block_y + block_hole)
            ):
                print("hit2")
                # keep_going = False

            x = x + 1

        # Draw picture and update display
        screen.fill(pygame.color.Color("Black"))
        pygame.draw.rect(screen, pygame.color.Color(heli_color), (heli_x, int(heli_y), heli_size, heli_size))

        for i in range(0, len(terrain)):
            block_x = terrain[i][0]
            block_y = terrain[i][1]
            block_hole = terrain[i][2]
            pygame.draw.rect(screen, pygame.color.Color("Orange"), (block_x, 0, 51, block_y))
            pygame.draw.rect(
                screen,
                pygame.color.Color("Orange"),
                (block_x, block_y + block_hole, 51, height - (block_y + block_hole)),
            )

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    # The game loop ends here.
    pygame.quit()


# Main hook
if __name__ == "__main__":
    run_game()
