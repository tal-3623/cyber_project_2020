import socket
import time

import pygame

import Constants
import menu
from Spirit import MySpirit, SpiritType
from input import Buttons


def draw_image(screen, image: str, x_pos: int, y_pos: int, colorkey: tuple = None):
    img = pygame.image.load(image).convert()
    if colorkey is not None:
        img.set_colorkey(colorkey)
    screen.blit(img, (x_pos, y_pos))


def receive_list_of_spirits(my_socket: socket.socket):
    rec = ''
    l = pygame.sprite.Group()
    while True:
        char = str(my_socket.recv(1).decode())
        rec += char
        if char == '@':
            break
    list_of_parts = rec.split('#')
    did_quit = bool(int(list_of_parts[0]))
    game_state = int(list_of_parts[1])
    list_of_spirits = list_of_parts[2].split('*')
    for spirit in list_of_spirits:
        if spirit == '':
            break

        x = int(spirit[0:4])
        y = int(spirit[4:8])
        file_name = spirit[8:]
        l.add(MySpirit(x, y, 0, 0, 0, 0, 255, file_name, SpiritType.UNKNOWN))
    return l, did_quit, game_state


def init():
    pygame.init()
    size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(Constants.GAME_NAME)
    draw_image(screen, Constants.BACKGROUND, 0, 0, )
    pygame.display.flip()
    return screen


def main():
    screen = init()
    button = Buttons(False)
    button.update()
    m = menu.Menu()
    while True:
        did_quit, is_arrows = m.run(button, screen)
        if did_quit:
            break
        my_socket = socket.socket()
        is_connected = False
        while not is_connected:
            try:
                my_socket.connect((Constants.SERVER_IP, Constants.SERVER_PORT))
                is_connected = True
            except:
                pass
        my_socket.send(str(int(is_arrows)).encode())
        draw_image(screen, 'stick_AME\\waiting_for_opponent.png', 0, 0)
        pygame.display.flip()
        while True:
            button.update()
            if button.did_quit:
                return
            r = my_socket.recv(10).decode()
            if r == 'start game':
                break


        did_other_player_quit = False
        while not button.did_quit and not did_other_player_quit:
            button.send_input_to_server(my_socket)
            draw_image(screen, Constants.BACKGROUND, 0, 0, )
            list_of_spirits, did_other_player_quit, game_state = receive_list_of_spirits(my_socket)
            list_of_spirits.draw(screen)
            pygame.display.flip()
            if game_state == 1:
                draw_image(screen, 'stick_AME\\you_won_screen.png', 0, 0)
                pygame.display.flip()
                time.sleep(Constants.END_GAME_SCREEN_TIME)
                break
            elif game_state == 2:
                draw_image(screen, 'stick_AME\\you_lose_screen.png', 0, 0)
                pygame.display.flip()
                time.sleep(Constants.END_GAME_SCREEN_TIME)
                break
        button.did_quit = False


if __name__ == '__main__':
    main()
