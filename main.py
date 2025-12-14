import sys
import pygame
from pygame.sprite import Group, Sprite

from logger import log_state, log_event

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

from asteroidfield import AsteroidField

from asteroid import Asteroid
from player import Player
from shot import Shot


# I think a better structure would be something along the lines of `while True: state = game_loop(state)`


def game_loop(
    screen: pygame.Surface,  #
    dt: float,
    clock: pygame.time.Clock,
    updatable,
    drawable,
    asteroids,
    player: Player,
    shots,
):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collides(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        pass

        for shot in shots:
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

    # making groups
    # this has unknown types
    updatable = Group()
    drawable = Group()
    asteroids = Group()
    shots = Group()

    # setting Player groups
    Player.containers = [updatable, drawable]

    # setting up Asteroids
    Asteroid.containers = [updatable, drawable, asteroids]
    AsteroidField.containers = [updatable]

    # setting up shots
    Shot.containers = [updatable, drawable, shots]

    # making the field
    asteroid_field = AsteroidField()

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
        updatable=updatable,
        drawable=drawable,
        asteroids=asteroids,
        player=player,
        shots=shots,
    )


if __name__ == "__main__":
    main()
