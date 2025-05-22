import pygame
import math

class Bullet:
    def __init__(self, pos, angle, image_path, speed=8):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.angle = angle
        self.speed = speed

        rad = math.radians(angle)
        self.velocity = pygame.Vector2(
            math.sin(rad),
            -math.cos(rad)
        ) * self.speed

    def update(self):
        self.pos += self.velocity
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)