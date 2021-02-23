import socket
import threading

import pygame

import Constants
from input import Buttons
from map_configoration import select_configuration
from offline_game import get_list_of_spirit


def send_list_of_spirits(player_1_socket: socket.socket, player_2_socket: socket.socket, player_1_buttons: Buttons,
                         player_2_buttons: Buttons, list_of_spirits, game_state):
    did_quit = str(int(player_1_buttons.did_quit or player_2_buttons.did_quit))
    game_state = str(game_state)
    list_of_spirits_encode = ''
    for spirit in list_of_spirits:
        list_of_spirits_encode += str(spirit.rect.x).zfill(4) + str(spirit.rect.y).zfill(4) + str(spirit.file_name)
        list_of_spirits_encode += '*'

    msg1 = (did_quit + '#' + game_state + '#' + list_of_spirits_encode + '#@').encode()
    if game_state == '1':
        game_state = '2'
    elif game_state == '2':
        game_state = '1'
    msg2 = (did_quit + '#' + game_state + '#' + list_of_spirits_encode + '#@').encode()
    player_1_socket.send(msg1)
    player_2_socket.send(msg2)


def play_game(player_1_socket: socket.socket, player_2_socket: socket.socket, player_1_buttons: Buttons,
              player_2_buttons: Buttons, player1_is_arrows: bool, player2_is_arrows: bool):
    list_of_spirit = pygame.sprite.Group()
    # player_one = Player(1, True, player1_is_arrows)
    # player_two = Player(2, True, player2_is_arrows)
    # floor = Block(-3, 630, 'Block.png')
    # b1 = Block(201, 360, 'Block._2png.png')
    # b2 = Block(500, 360, 'Block._2png.png')
    # list_of_spirit.add(b2)
    # list_of_spirit.add(b1)
    # list_of_spirit.add(floor)
    # for spirit in [player_one.player_head, player_one.player_body, player_one.player_legs, player_two.player_head,
    #                player_two.player_body, player_two.player_legs]:
    #     list_of_spirit.add(spirit)
    player_one, player_two = select_configuration(list_of_spirit, player1_is_arrows, player2_is_arrows)
    while True:
        if player_1_buttons.did_quit or player_2_buttons.did_quit:
            break
        if player_one.is_dead():
            game_state = 2
        elif player_two.is_dead():
            game_state = 1
        else:
            game_state = 0
        player_1_buttons.receive_input_from_client(player_1_socket)
        player_2_buttons.receive_input_from_client(player_2_socket)
        list_of_spirit = get_list_of_spirit(player_1_buttons, player_2_buttons, list_of_spirit, player_one, player_two,
                                            True)
        send_list_of_spirits(player_1_socket, player_2_socket, player_1_buttons, player_2_buttons, list_of_spirit,
                             game_state)
        if game_state != 0:
            break


def main():
    main_server = socket.socket()
    main_server.bind(('0.0.0.0', Constants.SERVER_PORT))
    main_server.listen(20)
    while True:
        socket_1, address_1 = main_server.accept()
        is_arrows_player_1 = bool(int(socket_1.recv(1).decode()))

        socket_2, address_2 = main_server.accept()
        is_arrows_player_2 = bool(int(socket_2.recv(1).decode()))

        socket_1.send('start game'.encode())
        socket_2.send('start game'.encode())
        player_2_buttons = Buttons(True)
        player_1_buttons = Buttons(True)
        game = threading.Thread(target=play_game, args=(
            socket_1, socket_2, player_1_buttons, player_2_buttons, is_arrows_player_1, is_arrows_player_2))
        game.start()


if __name__ == '__main__':
    main()
