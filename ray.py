import pygame
import math
from config import Config, Colors
from maps import world_map

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - Config.FOV / 2
    xo, yo = player_pos
    for ray in range(Config.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(Config.MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(sc, Colors.gray, player_pos, (x,y), 1)

            if (x // Config.TILE * Config.TILE, y // Config.TILE * Config.TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)

                proj_height = min(Config.PROJ_COEFF / (depth + 0.0001), Config.HEIGHT)
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)

                pygame.draw.rect(sc, color, (ray * Config.SCALE, Config.HEIGHT // 2 - proj_height // 2, Config.SCALE, proj_height))
                break
        cur_angle += Config.DELTA_ANGLE