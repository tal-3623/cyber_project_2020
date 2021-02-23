import math

import pygame

import Constants
# from Player import Player
from Spirit import MySpirit, SpiritType

MAX_SPEED_X = 60

MAX_SPEED_Y = 60


class Arrow(MySpirit):
    def __init__(self, player, mouse_x: int, mouse_y: int):
        x_diff = mouse_x - player.player_body.rect.midtop[0]
        y_diff = mouse_y - player.player_body.rect.midright[1]
        if x_diff > 0:
            x = player.player_body.rect.midright[0]
        else:
            x = player.player_body.rect.midleft[0] - 40

        y = player.player_body.rect.midleft[1] - 20
        vx = x_diff / 8
        vy = y_diff / 8
        if abs(vx) > MAX_SPEED_X:
            vx = math.copysign(MAX_SPEED_X, vx)
        if abs(vy) > MAX_SPEED_Y:
            vy = math.copysign(MAX_SPEED_Y, vy)

        ax = 0
        ay = Constants.G / 1.5
        colorkey = 0
        file_name = 'stick_AME\\Arrow000.png'
        type = SpiritType.ARROW
        super().__init__(x, y, vx, vy, ax, ay, colorkey, file_name, type)

    def update_angle(self):
        angle = math.degrees(math.atan2(self.vy * -1, self.vx)) * -1
        angle += 41
        if angle < 0:
            angle += 360
        elif angle > 360:
            angle = angle % 360

        angle = int(angle)
        self.file_name = 'stick_AME\\Arrow' + str(angle).zfill(3) + '.png'

    def update_loc(self):
        super().update_loc()
        self.update_angle()
        self.image = pygame.image.load(self.file_name)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_damage(self):
        return (self.vx ** 2 + self.vy ** 2) ** (1 / 2.5)
