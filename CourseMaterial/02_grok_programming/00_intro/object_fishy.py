import random

import pygame


class User(object):
    def __init__(self, x: int, y: int, lives: int) -> None:
        self.x = x
        self.y = y
        self.size = 20
        self.lives = lives

    def move_left(self) -> None:
        self.x = self.x - 3

    def move_right(self) -> None:
        self.x = self.x + 3

    def move_up(self) -> None:
        self.y = self.y - 3

    def move_down(self) -> None:
        self.y = self.y + 3

    def grow(self) -> None:
        self.size = self.size * 1.1

    def die(self) -> None:
        self.size = 20
        self.lives = self.lives - 1
        self.x = 500
        self.y = 500

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_size(self) -> int:
        return int(self.size)

    def get_lives(self) -> int:
        return self.lives


class Dinner(object):
    def __init__(self):
        self.y = random.randint(0, 1000)
        self.size = random.randint(10, 70)
        if random.randint(0, 1) == 1:
            self.speed = random.randint(3, 7)
            self.x = 0
        else:
            self.speed = random.randint(3, 7) * -1
            self.x = 0

    def move(self) -> None:
        self.x = self.x + self.speed

    def reset(self) -> None:
        self.y = random.randint(0, 1000)
        self.size = random.randint(10, 70)
        if random.randint(0, 1) == 1:
            self.speed = random.randint(3, 7)
            self.x = 0
        else:
            self.speed = random.randint(3, 7) * -1
            self.x = 1000

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_size(self) -> int:
        return int(self.size)


def collide(x1: int, y1: int, size1: int, x2: int, y2: int, size2: int) -> bool:
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance > size1 + size2:
        return False
    else:
        return True


def run_game():
    # Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 1000
    height = 1000
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    fishy = User(500, 500, 3)
    enemies = [Dinner() for _ in range(0, 10)]

    # The game loop starts here.
    keep_going = True
    while keep_going and fishy.get_lives() > 0:
        # User Input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            fishy.move_right()
        if key[pygame.K_LEFT]:
            fishy.move_left()
        if key[pygame.K_UP]:
            fishy.move_up()
        if key[pygame.K_DOWN]:
            fishy.move_down()

        # Move
        for enemy in enemies:
            enemy.move()

            # Check for collisions
            if enemy.get_x() > 1000 or enemy.get_x() < 0:
                enemy.reset()

            if collide(enemy.get_x(), enemy.get_y(), enemy.get_size(), fishy.get_x(), fishy.get_y(), fishy.get_size()):
                if enemy.get_size() > fishy.get_size():
                    enemy.reset()
                    fishy.die()
                else:
                    enemy.reset()
                    fishy.grow()

        # Draw picture and update display
        screen.fill(pygame.color.Color("Black"))

        pygame.draw.circle(screen, pygame.color.Color("Red"), (fishy.get_x(), fishy.get_y()), fishy.get_size())
        for enemy in enemies:
            pygame.draw.circle(screen, pygame.color.Color("Pink"), (enemy.get_x(), enemy.get_y()), enemy.get_size())

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    # The game loop ends here.
    pygame.quit()


# Main hook
if __name__ == "__main__":
    run_game()
