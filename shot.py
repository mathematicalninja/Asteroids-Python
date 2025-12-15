import pygame
from pygame.math import Vector2
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADUIS


class Shot(CircleShape):
    def __init__(
        self,  #
        pos: Vector2,
        inital_speed: float,
        unit_velocity: pygame.Vector2,
        radius: float = SHOT_RADUIS,  # allows varied shot sizes.
    ):
        super().__init__(pos.x, pos.y, radius)

        self.velocity: pygame.Vector2 = unit_velocity * inital_speed
        self.unit_velocity = unit_velocity
        self.speed = inital_speed

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,  #
            color="green",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )
        pass

    def update(self, dt: float):
        self.position += self.velocity * dt

    pass
