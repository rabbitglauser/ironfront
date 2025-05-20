# game/tank.py

import pygame
import math

class Tank:
    def __init__(self, x, y, image_path):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        self.pos = pygame.math.Vector2(x, y)

        self.angle = 0
        self.target_angle = 0
        self.rotation_speed = 2
        self.speed = 2

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_d]:
            self.angle += self.rotation_speed

        self.angle %= 360

        if keys[pygame.K_w]:
            self.move_forward()
        if keys[pygame.K_s]:
            self.move_backward()

        self.update_image()

    def move_forward(self):
        direction = pygame.math.Vector2(
            math.sin(math.radians(self.angle)),
            -math.cos(math.radians(self.angle))
        )
        self.pos += direction * self.speed
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def move_backward(self):
        direction = pygame.math.Vector2(
            math.sin(math.radians(self.angle)),
            -math.cos(math.radians(self.angle))
        )
        self.pos -= direction * self.speed
        self.rect.center = (int(self.pos.x), int(self.pos.y))

    def rotate_smoothly(self):
        # Rotate toward target_angle
        angle_diff = (self.target_angle - self.angle + 360) % 360
        if angle_diff > 180:
            angle_diff -= 360

        if abs(angle_diff) > self.rotation_speed:
            self.angle += self.rotation_speed * (1 if angle_diff > 0 else -1)
        else:
            self.angle = self.target_angle

        self.angle %= 360
        self.update_image()

    def update_image(self):
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
