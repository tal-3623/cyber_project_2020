import socket

import pygame


class Buttons:
    def __init__(self, is_server: bool):
        # defualt value's:
        if not is_server:
            self.events = pygame.event.get()
            self.did_quit = False
            self.keys_pressed = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            self.mouse_x_pos = mouse_pos[0]
            self.mouse_y_pos = mouse_pos[1]
            self.mouse_left_button = False
            self.mouse_right_button = False
        else:
            self.events = None
            self.did_quit = False
            self.keys_pressed = None
            mouse_pos = None
            self.mouse_x_pos = None
            self.mouse_y_pos = None
            self.mouse_left_button = False
            self.mouse_right_button = False

    def update(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.did_quit = True
        self.keys_pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_x_pos = mouse_pos[0]
        self.mouse_y_pos = mouse_pos[1]
        self.mouse_left_button = pygame.mouse.get_pressed()[0] == 1
        self.mouse_right_button = pygame.mouse.get_pressed()[2] == 1
        #     call this function periodically

    def send_input_to_server(self, client_socket: socket.socket):
        self.update()
        did_quit = str(int(self.did_quit))  # 0 / 1
        keys_pressed = str(self.keys_pressed).strip('(').strip(')')
        mouse = str(self.mouse_x_pos).zfill(4) + str(self.mouse_y_pos).zfill(4) + str(
            int(self.mouse_right_button)) + str(int(
            self.mouse_left_button))
        final = '@'

        msg = '#'.join((did_quit, keys_pressed, mouse, final)).encode()
        client_socket.send(msg)

    def receive_input_from_client(self, server_socket: socket.socket):
        rec = ''
        while True:
            char = str(server_socket.recv(1).decode())
            rec += char
            if char == '@':
                break
        list_of_parts = rec.split('#')
        self.did_quit = bool(int(list_of_parts[0]))
        self.keys_pressed = list(list_of_parts[1].split(','))
        self.mouse_x_pos = int(list_of_parts[2][0:4])
        self.mouse_y_pos = int(list_of_parts[2][4:8])
        self.mouse_right_button = bool(int(list_of_parts[2][8]))
        self.mouse_left_button = bool(int(list_of_parts[2][9]))
        for i in range(0, len(self.keys_pressed)):
            self.keys_pressed[i] = bool(int(self.keys_pressed[i]))
