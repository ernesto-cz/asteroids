import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collition(self,CircleShape):
        distance = pygame.Vector2.distance_to(self.position, CircleShape.position)
        r1 = self.radius
        r2 = CircleShape.radius
        if distance <= r1 + r2:
            return True
        return False
