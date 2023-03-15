from config import Config, Colors
from player import Player
from maps import world_map
from ray import ray_casting
###############################
import pygame
import math

pygame.init()
sc = pygame.display.set_mode(size=(Config.WIDTH, Config.HEIGHT))
clock = pygame.time.Clock()

player = Player()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(Colors.black)

    ray_casting(sc, player.pos, player.angle)

    pygame.draw.circle(sc, Colors.green, (int(player.x)//4, int(player.y)//4), 12//4)
    pygame.draw.line(sc, Colors.green, player.map_pos, ((player.x//4 + Config.WIDTH * math.cos(player.angle)/8),
                                                        (player.y//4 + Config.WIDTH * math.sin(player.angle)/8)))

    for x,y in world_map:
        pygame.draw.rect(sc, Colors.gray, (x//4, y//4, Config.TILE//4, Config.TILE//4), 2)
    pygame.display.flip()
    clock.tick(Config.FPS)