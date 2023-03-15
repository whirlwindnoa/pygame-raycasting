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

    #pygame.draw.circle(sc, Colors.green, (int(player.x), int(player.y)), 12)
    #pygame.draw.line(sc, Colors.green, player.pos, (player.x + Config.WIDTH * math.cos(player.angle),
    #                                                player.y + Config.WIDTH * math.sin(player.angle)))

    #for x,y in world_map:
    #    pygame.draw.rect(sc, Colors.gray, (x, y, Config.TILE, Config.TILE), 2)
    pygame.display.flip()
    clock.tick(Config.FPS)
