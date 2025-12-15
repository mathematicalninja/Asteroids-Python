import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,  #
            color="red",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )
        pass

    def update(self, dt: float):
        self.position += self.velocity * dt

    pass

    def split(self, shot):
        # idea: takes the shot's incomming direction and uses that as the "split axis"
        # Basic physics, it should preserve momentum.
        # Shot's momentum is split between the two shots

        # idea: medium should split into 3 tiny asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius <= ASTEROID_MIN_RADIUS:
            # split 3
            pass

        log_event("asteroid_split")
