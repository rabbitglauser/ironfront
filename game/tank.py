import pygame
import math
from bullet import Bullet

class Tank:
    def __init__(self, x, y, body_path, turret_path):
        self.body_original = pygame.image.load(body_path).convert_alpha()
        self.turret_original = pygame.image.load(turret_path).convert_alpha()
        self.pos = pygame.math.Vector2(x, y)
        self.angle = 0
        self.turret_angle = 0
        self.rotation_speed = 2
        self.speed = 2

        # EDIT THESE IF YOUR IMAGE IS DIFFERENT
        width, height = self.turret_original.get_width(), self.turret_original.get_height()
        self.body_pivot = (self.body_original.get_width() // 2, self.body_original.get_height() // 2)
        self.turret_pivot = (width // 2, height)          # base of barrel in image
        self.barrel_tip_pixel = (width // 2, 0)           # tip of barrel in image

        self.bullets = []
        self.bullet_image_path = "assets/PNG/Bullets/bulletGreen.png"
        self.shoot_cooldown = 0

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

    def get_barrel_tip_pos(self):
        # Use the same math as drawing!
        pivot = pygame.math.Vector2(self.turret_pivot)
        tip = pygame.math.Vector2(self.barrel_tip_pixel)
        offset = tip - pivot
        rotated_offset = offset.rotate(-self.turret_angle)
        return self.pos + rotated_offset

    def update_turret_angle(self, mouse_pos):
        dx = mouse_pos[0] - self.pos.x
        dy = mouse_pos[1] - self.pos.y
        self.turret_angle = math.degrees(math.atan2(dx, -dy)) % 360

    def update_bullets(self, screen_rect):
        for bullet in self.bullets[:]:
            bullet.update()
            if not screen_rect.colliderect(bullet.rect):
                self.bullets.remove(bullet)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self):
        if self.shoot_cooldown == 0:
            start_pos = self.get_barrel_tip_pos()
            bullet = Bullet(start_pos, self.turret_angle, self.bullet_image_path)
            self.bullets.append(bullet)
            self.shoot_cooldown = 15

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
        self.blit_rotate_pivot(surface, self.body_original, self.pos, self.angle, self.body_pivot)
        self.blit_rotate_pivot(surface, self.turret_original, self.pos, self.turret_angle, self.turret_pivot)
        for bullet in self.bullets:
            bullet.draw(surface)
        # Debug: draw tank center and barrel tip
        tip_world = self.get_barrel_tip_pos()
        pygame.draw.circle(surface, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 6)  # Tank center/pivot
        pygame.draw.circle(surface, (0, 255, 0), (int(tip_world.x), int(tip_world.y)), 6)  # Barrel tip