import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

import random

from shot import Shot


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

    def split(self, shot: Shot):
        # idea: takes the shot's incoming direction and uses that as the "split axis"
        # Basic physics, it should preserve momentum.
        # Shot's momentum is split between the two shots

        # idea: medium should split into 3 tiny asteroids
        self.kill()
        speed = self.velocity.length()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # small asteroids don't "eat" the shot, they slow it.
            Shot(
                pos=self.position,  #
                unit_velocity=shot.unit_velocity,
                inital_speed=speed,
            )
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        A = Asteroid(
            x=self.position.x,  #
            y=self.position.y,  #
            radius=new_radius,
        )
        A.velocity = self.velocity.rotate(random_angle)
        B = Asteroid(
            x=self.position.x,  #
            y=self.position.y,  #
            radius=new_radius,
        )
        B.velocity = self.velocity.rotate(-random_angle)
        if new_radius <= ASTEROID_MIN_RADIUS:
            C = Asteroid(
                x=self.position.x,  #
                y=self.position.y,  #
                radius=new_radius,
            )
            shot_direction = shot.unit_velocity
            C.velocity = shot_direction * speed

        log_event("asteroid_split")
