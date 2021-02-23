import pygame

import Constants
from Block import Block
from Player import Player
from Spirit import SpiritType
from input import Buttons


def draw_image(screen, image: str, x_pos: int, y_pos: int, colorkey: tuple = None):
    img = pygame.image.load(image).convert()
    if colorkey is not None:
        img.set_colorkey(colorkey)
    screen.blit(img, (x_pos, y_pos))


def init():
    pygame.init()
    size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(Constants.GAME_NAME)
    draw_image(screen, Constants.BACKGROUND, 0, 0, )
    pygame.display.flip()
    return screen


def get_list_of_spirit(player_one_button: Buttons, player_two_button, list_of_spirit: pygame.sprite.Group,
                       player_one: Player,
                       player_two: Player, is_online: bool) -> pygame.sprite.Group:
    if not is_online:
        player_one.update_loc()
        player_two.update_loc()
        player_one.periodic_behavior(player_one_button, None, list_of_spirit, player_two)
        player_two.periodic_behavior(player_one_button, None, list_of_spirit, player_one)
        for spirit in list_of_spirit:
            if spirit.type == SpiritType.ARROW:
                spirit.update_loc()
                list_of_collided = pygame.sprite.spritecollide(spirit, list_of_spirit, False)
                if spirit.is_out_of_bounds():
                    spirit.kill()
                    continue
                for spirit_that_collided in list_of_collided:
                    if spirit.type == spirit_that_collided.type:
                        continue
                    elif spirit_that_collided.type == SpiritType.BLOCK:
                        spirit.kill()
            # elif spirit.type == SpiritType.BLOCK:
            #   pass
    else:
        player_one.update_loc()
        player_two.update_loc()
        player_one.periodic_behavior(player_one_button, player_two_button, list_of_spirit, player_two)
        player_two.periodic_behavior(player_one_button, player_two_button, list_of_spirit, player_one)
        for spirit in list_of_spirit:
            if spirit.type == SpiritType.ARROW:
                spirit.update_loc()
                list_of_collided = pygame.sprite.spritecollide(spirit, list_of_spirit, False)
                if spirit.is_out_of_bounds():
                    spirit.kill()
                    continue
                for spirit_that_collided in list_of_collided:
                    if spirit.type == spirit_that_collided.type:
                        continue
                    elif spirit_that_collided.type == SpiritType.BLOCK:
                        spirit.kill()
            # elif spirit.type == SpiritType.BLOCK:
            #   pass

    return list_of_spirit


def main():
    screen = init()
    button = Buttons(False)
    list_of_spirit = pygame.sprite.Group()
    player_one = Player(1, False)
    player_two = Player(2, False)
    floor = Block(-3, 630, 'Block.png')
    # b1 = Block(201, 360, 'Block._2png.png')
    b2 = Block(500, 360, 'Block._2png.png')
    list_of_spirit.add(b2)
    # list_of_spirit.add(b1)
    list_of_spirit.add(floor)
    for spirit in [player_one.player_head, player_one.player_body, player_one.player_legs, player_two.player_head,
                   player_two.player_body, player_two.player_legs]:
        list_of_spirit.add(spirit)
        t = 0
    while not button.did_quit:
        # print(time.time() - t)
        # t = time.time()
        draw_image(screen, Constants.BACKGROUND, 0, 0)
        list_of_spirit.draw(screen)
        button.update()
        list_of_spirit = get_list_of_spirit(button, None, list_of_spirit, player_one, player_two, False)
        pygame.display.flip()
        if player_one.is_dead():
            break
        elif player_two.is_dead():
            break


if __name__ == '__main__':
    main()
