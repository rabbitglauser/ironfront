# game/main.py

import pygame
import sys
from map import game_map
from tank import Tank

# Init
pygame.init()
TILE_SIZE = 64
MAP_WIDTH = len(game_map[0])
MAP_HEIGHT = len(game_map)
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ironfront - Tank Movement")

# Load environment tiles
grass = pygame.image.load("assets/PNG/Environment/grass.png")
dirt = pygame.image.load("assets/PNG/Environment/dirt.png")
sand = pygame.image.load("assets/PNG/Environment/sand.png")
wall = pygame.image.load("assets/PNG/Environment/treeSmall.png")

tile_textures = {
    0: grass,
    1: dirt,
    2: sand,
    3: wall
}

# Create player tank
player = Tank(x=100, y=100, image_path="assets/PNG/Tanks/tankGreen.png")

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))

    # Draw map
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            texture = tile_textures.get(tile)
            if texture:
                screen.blit(texture, (x * TILE_SIZE, y * TILE_SIZE))

    # Handle keys and movement
    player.handle_keys()

    # Draw tank
    player.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
sys.exit()
