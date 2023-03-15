from config import Config
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = Config.player_pos
        self.angle = Config.player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += Config.player_speed * cos_a
            self.y += Config.player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -Config.player_speed * cos_a
            self.y += -Config.player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += Config.player_speed * sin_a
            self.y += -Config.player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -Config.player_speed * sin_a
            self.y += Config.player_speed * cos_a

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02