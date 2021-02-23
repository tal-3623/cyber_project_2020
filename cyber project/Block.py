import pygame

from Spirit import SpiritType, MySpirit


class Block(MySpirit):
    def __init__(self, x: int, y: int, file_name: str):
        vx = 0
        vy = 0
        ax = 0
        ay = 0
        colorkey = (255, 244, 233)
        type = SpiritType.BLOCK
        super().__init__(x, y, vx, vy, ax, ay, colorkey, file_name, type)

    def periodic_behavior(self, list_of_spirit: pygame.sprite.Group):
        list_of_collided = pygame.sprite.spritecollide(self, list_of_spirit, False)
        for spirit_that_collided in list_of_collided:
            if spirit_that_collided.type == self.type:
                continue
            if spirit_that_collided.type == SpiritType.ARROW:
                spirit_that_collided.kill()
