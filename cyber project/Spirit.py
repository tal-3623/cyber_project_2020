import enum

import pygame

import Constants
import Direction


class SpiritType(enum.Enum):
    PLAYER_1_LEGS = 1
    PLAYER_1_BODY = 2
    PLAYER_1_HEAD = 3
    PLAYER_2_LEGS = 4
    PLAYER_2_BODY = 5
    PLAYER_2_HEAD = 6
    ARROW = 7
    BLOCK = 8
    UNKNOWN = 9


class MySpirit(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, vx, vy, ax, ay, colorkey, file_name: str, type: SpiritType):
        super(MySpirit, self).__init__()
        self.vx = vx
        self.vy = vy
        self.ay = ay
        self.ax = ax
        self.type = type
        self.file_name = file_name
        if not self.type in [SpiritType.ARROW, SpiritType.PLAYER_1_LEGS, SpiritType.PLAYER_2_LEGS]:
            self.image = pygame.image.load(file_name)
        else:
            self.image = pygame.image.load(file_name)
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.my_rect = Direction.Rect(self.rect)

    def update_loc(self):
        self.vx += self.ax
        self.vy += self.ay
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)
        self.my_rect = Direction.Rect(self.rect)

    def is_out_of_bounds(self) -> bool:
        if self.rect.x + self.rect.width < 0:
            print('out')
            return True
        if self.rect.x > Constants.WINDOW_WIDTH:
            print('out')
            return True
        if self.rect.y > Constants.WINDOW_HEIGHT:
            print('out')
            return True
        return False
