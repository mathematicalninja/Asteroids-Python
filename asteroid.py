import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


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
