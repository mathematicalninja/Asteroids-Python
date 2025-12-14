from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED
import pygame


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x=x, y=y, radius=PLAYER_RADIUS)
        self.rotation: float = 0
        pass

    def triangle(self):
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(self.rotation)
        right: pygame.Vector2 = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(
        self,
        screen: pygame.Surface,
    ):
        colour = "white"
        pygame.draw.polygon(
            surface=screen,  #
            color=colour,
            points=self.triangle(),
            width=LINE_WIDTH,
        )

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        # vim keys or wasd
        if keys[pygame.K_h] or keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_l]:
            self.rotate(dt)
