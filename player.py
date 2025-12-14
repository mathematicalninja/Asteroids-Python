from pygame.math import Vector2
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADUIS,
)
import pygame

from shot import Shot


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

        #  wasd or vim keys
        if keys[pygame.K_a] or keys[pygame.K_h]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_l]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_k]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_j]:
            self.move(-dt)

        if keys[pygame.K_SPACE] or keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            self.shoot()

        if keys[pygame.K_n]:
            self.shoot()

    def move(self, dt: float):
        self.position += self.get_rotation_vector() * PLAYER_SPEED * dt

    def get_rotation_vector(self) -> Vector2:
        return Vector2(0, 1).rotate(self.rotation)

    def shoot(self):
        rotation_vector = self.get_rotation_vector()
        pos = self.position + rotation_vector * self.radius
        shot = Shot(
            x=pos.x,  #
            y=pos.y,
            velocity=self.get_rotation_vector() * PLAYER_SHOT_SPEED,
            radius=SHOT_RADUIS,
        )
        return shot
