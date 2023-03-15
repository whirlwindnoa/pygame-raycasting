import math

# Essential constants
class Config:
    # Game Configuration
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    TILE = 100
    # Player Settings
    player_pos = (WIDTH // 2, HEIGHT // 2)
    player_angle = 0
    player_speed = 2

    # Ray Casting Configuration
    FOV = math.pi / 3
    NUM_RAYS = 60
    MAX_DEPTH = 800
    DELTA_ANGLE = FOV / NUM_RAYS

    DIST = NUM_RAYS / (2 * math.tan(FOV / 2))
    PROJ_COEFF = 4 * DIST * TILE
    SCALE = WIDTH // NUM_RAYS

class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    purple = (128, 0, 128)
    gray = (128, 128, 128)
