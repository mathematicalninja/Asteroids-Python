import pygame

from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

from player import Player


# I think a better structure would be something along the lines of `while True: state = game_loop(state)`


def game_loop(
    screen: pygame.Surface,  #
    dt: float,
    clock: pygame.time.Clock,
    player: Player,
):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")

        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        pass

        ticked = clock.tick(60)
        dt = ticked / 1000


def main():
    VERSION = pygame.version.ver

    # boot.dev print grading.
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # making the player.
    player = Player(
        x=SCREEN_WIDTH / 2,  #
        y=SCREEN_HEIGHT / 2,
    )

    # calling the game loop, so it's separated.
    game_loop(
        screen=screen,  #
        dt=dt,
        clock=clock,
        player=player,
    )


if __name__ == "__main__":
    main()
