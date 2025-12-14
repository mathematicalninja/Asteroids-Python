import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def game_loop(screen: pygame.Surface):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        pygame.display.flip()
        pass


def main():
    VERSION = pygame.version.ver

    # boot.dev print grading.
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_loop(screen)


if __name__ == "__main__":
    main()
