import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADUIS


class Shot(CircleShape):
    def __init__(
        self,  #
        x: float,
        y: float,
        velocity: pygame.Vector2,
        radius: float = SHOT_RADUIS,  # allows varied shot sizes.
    ):
        super().__init__(x, y, radius)

        self.velocity: pygame.Vector2 = velocity

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
