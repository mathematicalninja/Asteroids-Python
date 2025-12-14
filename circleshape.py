# to allow CircleShape to reference CircleShape
from __future__ import annotations

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface):
        # must override
        pass

    def update(self, dt: float):
        # must override
        pass

    def collides(self, other: CircleShape) -> bool:
        distance = self.position.distance_to(other.position)
        total_radii = self.radius + other.radius

        # soft edges to allow "skin of the teeth" flying.
        if distance < total_radii:
            return True
        return False
