import pygame
import math

class Tank:
    def __init__(self, x, y, body_path, turret_path):
        self.body_original = pygame.image.load(body_path).convert_alpha()
        self.turret_original = pygame.image.load(turret_path).convert_alpha()
        self.pos = pygame.math.Vector2(x, y)
        self.angle = 0
        self.turret_angle = 0
        self.rotation_speed = 2
        self.speed = 2

        # Set these to the center of the circle on your images!
        self.body_pivot = (self.body_original.get_width() // 2, self.body_original.get_height() // 2)
        self.turret_pivot = (self.turret_original.get_width() // 2, self.turret_original.get_height())

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

    def move_forward(self):
        direction = pygame.math.Vector2(
            math.sin(math.radians(self.angle)),
            -math.cos(math.radians(self.angle))
        )
        self.pos += direction * self.speed

    def move_backward(self):
        direction = pygame.math.Vector2(
            math.sin(math.radians(self.angle)),
            -math.cos(math.radians(self.angle))
        )
        self.pos -= direction * self.speed

    def update_turret_angle(self, mouse_pos):
        # Calculate angle from tank center to mouse position
        dx = mouse_pos[0] - self.pos.x
        dy = mouse_pos[1] - self.pos.y
        self.turret_angle = math.degrees(math.atan2(dx, -dy)) % 360

    def blit_rotate_pivot(self, surface, image, pos, angle, pivot):
        image_center = pygame.math.Vector2(image.get_width() / 2, image.get_height() / 2)
        offset = pygame.math.Vector2(pivot) - image_center
        rotated_image = pygame.transform.rotate(image, -angle)
        rotated_offset = offset.rotate(angle)
        rotated_rect = rotated_image.get_rect()
        blit_pos = (pos[0] - rotated_rect.width // 2 - rotated_offset.x,
                    pos[1] - rotated_rect.height // 2 - rotated_offset.y)
        surface.blit(rotated_image, blit_pos)

    def draw(self, surface):
        # Draw body with tank angle
        self.blit_rotate_pivot(surface, self.body_original, self.pos, self.angle, self.body_pivot)
        # Draw turret with turret angle (relative to world, not body)
        self.blit_rotate_pivot(surface, self.turret_original, self.pos, self.turret_angle, self.turret_pivot)