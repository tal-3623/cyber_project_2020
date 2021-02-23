import random

import pygame

from Block import Block
from Player import Player


def select_configuration(list_of_spirit: pygame.sprite.Group, player1_is_arrows: bool, player2_is_arrows: bool):
    arr_of_configuration = [configuration1]
    return arr_of_configuration[random.randint(0, len(arr_of_configuration) - 1)](list_of_spirit, player1_is_arrows,
                                                                                  player2_is_arrows)


def configuration1(list_of_spirit: pygame.sprite.Group, player1_is_arrows: bool, player2_is_arrows: bool):
    player_one = Player(1, True, player1_is_arrows)
    player_two = Player(2, True, player2_is_arrows)
    floor = Block(0, 680, 'stick_AME\\floor.png')
    b1 = Block(201, 450, 'stick_AME\\block_200_60.png')
    b2 = Block(800, 450, 'stick_AME\\block_200_60.png')
    b3 = Block(500, 250, 'stick_AME\\block_200_60.png')
    b4 = Block(110, 150, 'stick_AME\\block_200_60.png')
    b5 = Block(1090, 150, 'stick_AME\\block_200_60.png')
    for b in [b1, b2, b3, b4, b5]:
        list_of_spirit.add(b)
    list_of_spirit.add(floor)
    for spirit in [player_one.player_head, player_one.player_body, player_one.player_legs, player_two.player_head,
                   player_two.player_body, player_two.player_legs]:
        list_of_spirit.add(spirit)
    return player_one, player_two


def configuration2(list_of_spirit: pygame.sprite.Group, player1_is_arrows: bool, player2_is_arrows: bool):
    pass
