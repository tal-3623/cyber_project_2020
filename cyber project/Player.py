import pygame

import Arrow
import Constants
from Direction import get_collision_direction, Direction, Rect
from Spirit import SpiritType, MySpirit
from Timer import Timer
from input import Buttons


class PlayerLegs(MySpirit):
    WALK_STEP = 2.23

    def __init__(self, player_num: int):
        self.player_num = player_num
        if player_num == 1:
            type = SpiritType.PLAYER_1_LEGS
            x = Constants.PLAYER_ONE_STARTING_X_LEGS
            y = Constants.PLAYER_ONE_STARTING_Y_LEGS
        else:  # player num is 2
            type = SpiritType.PLAYER_2_LEGS
            x = Constants.PLAYER_TWO_STARTING_X_LEGS
            y = Constants.PLAYER_TWO_STARTING_Y_LEGS
        vx = 0
        vy = 0
        ax = 0
        ay = 0
        colorkey = Constants.COLOR_KEY_BACKGROUND
        file_name = 'walk2\\wallk00.png'
        self.index = 0

        super().__init__(x, y, vx, vy, ax, ay, colorkey, file_name, type)

    def set_x_y(self, x: int, y: int):
        self.rect.x = x
        self.rect.y = y

    def walk(self):
        if self.vx > 0:
            self.index += self.WALK_STEP
        else:
            self.index -= self.WALK_STEP
        if self.index > 60:
            self.index = 0
        elif self.index < 0:
            self.index = 60
        image_name = 'walk2\\wallk' + str(int(self.index)).zfill(2) + '.png'
        self.file_name = image_name
        self.image = pygame.image.load(image_name)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlayerBody(MySpirit):
    def __init__(self, player_num: int):
        if player_num == 1:
            x = Constants.PLAYER_ONE_STARTING_X_BODY
            y = Constants.PLAYER_ONE_STARTING_Y_BODY
            vx = 0
            vy = 0
            ax = 0
            ay = 0
            type = SpiritType.PLAYER_1_BODY
        else:
            x = Constants.PLAYER_TWO_STARTING_X_BODY
            y = Constants.PLAYER_TWO_STARTING_Y_BODY
            vx = 0
            vy = 0
            ax = 0
            ay = 0
            type = SpiritType.PLAYER_2_BODY
        file_name = 'stick_AME\\bow and arrow ani00.png'
        colorkey = (255, 255, 255)
        self.index = 0
        self.PLAYER_X_DIFF_LEGS_BODY = 10
        super().__init__(x, y, vx, vy, ax, ay, colorkey, file_name, type)

    def set_x_y(self, x: int, y: int):
        self.rect.x = x + self.PLAYER_X_DIFF_LEGS_BODY
        self.rect.y = y + Constants.PLAYER_Y_DIFF_LEGS_BODY

    def reverse_aim(self, mouse_x: int, middle_x: int):
        if mouse_x - middle_x > 0:
            direction = Direction.RIGHT
            self.PLAYER_X_DIFF_LEGS_BODY = 10
        else:
            direction = Direction.LEFT
            self.PLAYER_X_DIFF_LEGS_BODY = -35

        if direction == Direction.RIGHT:
            if self.index == 0:
                pass
            else:
                self.index -= 1
            image_name = 'stick_AME\\bow and arrow ani' + str(int(self.index)).zfill(2) + '.png'
        else:
            if self.index == 0:
                pass
            else:
                self.index -= 1
            image_name = 'stick_AME\\bow and arrow ani mirror' + str(int(self.index)).zfill(2) + '.png'
        self.file_name = image_name
        self.image = pygame.image.load(image_name)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def aim(self, mouse_x: int, middle_x: int):

        if mouse_x - middle_x > 0:
            direction = Direction.RIGHT
            self.PLAYER_X_DIFF_LEGS_BODY = 10
        else:
            direction = Direction.LEFT
            self.PLAYER_X_DIFF_LEGS_BODY = -35

        if direction == Direction.RIGHT:
            if self.index == 22:
                pass
            else:
                self.index += 1
            image_name = 'stick_AME\\bow and arrow ani' + str(int(self.index)).zfill(2) + '.png'
        else:
            if self.index == 22:
                pass
            else:
                self.index += 1
            image_name = 'stick_AME\\bow and arrow ani mirror' + str(int(self.index)).zfill(2) + '.png'
        self.file_name = image_name
        self.image = pygame.image.load(image_name)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PlayerHead(MySpirit):
    def __init__(self, player_num: int):
        if player_num == 1:
            x = Constants.PLAYER_ONE_STARTING_X_HEAD
            y = Constants.PLAYER_ONE_STARTING_Y_HEAD
            vx = 0
            vy = 0
            ax = 0
            ay = 0
            type = SpiritType.PLAYER_1_HEAD
        else:
            x = Constants.PLAYER_TWO_STARTING_X_HEAD
            y = Constants.PLAYER_TWO_STARTING_Y_HEAD
            vx = 0
            vy = 0
            ax = 0
            ay = 0
            type = SpiritType.PLAYER_2_HEAD
        file_name = 'stick_AME\\HEAD0.png'
        colorkey = (255, 255, 255)
        self.PLAYER_X_DIFF_LEGS_HEAD = 20
        super().__init__(x, y, vx, vy, ax, ay, colorkey, file_name, type)

    def set_x_y(self, x: int, y: int):
        self.rect.x = x + self.PLAYER_X_DIFF_LEGS_HEAD
        self.rect.y = y + Constants.PLAYER_Y_DIFF_LEGS_HEAD

    def look(self, mouse_x: int, middle_x: int):
        if mouse_x - middle_x > 0:
            self.PLAYER_X_DIFF_LEGS_HEAD = 20
        else:
            self.PLAYER_X_DIFF_LEGS_HEAD = 5


class Player:
    def __init__(self, player_num: int, is_online: bool, is_arrows: bool):
        self.player_num = player_num
        self.player_legs = PlayerLegs(player_num)
        self.player_body = PlayerBody(player_num)
        self.player_head = PlayerHead(player_num)
        self.x = self.player_head.rect.x
        self.y = self.player_head.rect.y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = Constants.G
        self.player_spirits_types = [self.player_legs.type, self.player_body.type, self.player_head.type]
        self.collision_direction = Direction.NONE
        self.collision_diff = 0
        self.is_on_the_floor = False
        self.did_press_right = None
        self.did_press_left = None
        self.did_press_jump = None
        self.is_online = is_online
        self.health = 100
        self.is_aiming = False
        self.reloading_timer = Timer()
        self.is_arrows = is_arrows

    def update_loc(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += int(self.vx)
        self.y += int(self.vy)
        self.update_spirits()

    def update_spirits(self):
        for spirit in [self.player_legs, self.player_body, self.player_head]:
            spirit.vx = self.vx
            spirit.vy = self.vy
            spirit.ax = self.ax
            spirit.ay = self.ay
            spirit.set_x_y(self.x, self.y)
            spirit.my_rect = Rect(spirit.rect)
        self.collision_direction = Direction.NONE

    def periodic_behavior(self, player_one_button: Buttons, player_two_button,
                          list_of_spirit: pygame.sprite.Group, other_player):
        if self.player_num == 1:
            if self.is_online:
                if self.is_arrows:
                    self.did_press_right = player_one_button.keys_pressed[pygame.K_RIGHT]
                    self.did_press_left = player_one_button.keys_pressed[pygame.K_LEFT]
                    self.did_press_jump = player_one_button.keys_pressed[pygame.K_UP]
                else:
                    self.did_press_right = player_one_button.keys_pressed[pygame.K_d]
                    self.did_press_left = player_one_button.keys_pressed[pygame.K_a]
                    self.did_press_jump = player_one_button.keys_pressed[pygame.K_w]
                if other_player.is_arrows:
                    other_player.did_press_right = player_two_button.keys_pressed[pygame.K_RIGHT]
                    other_player.did_press_left = player_two_button.keys_pressed[pygame.K_LEFT]
                    other_player.did_press_jump = player_two_button.keys_pressed[pygame.K_UP]
                else:
                    other_player.did_press_right = player_two_button.keys_pressed[pygame.K_d]
                    other_player.did_press_left = player_two_button.keys_pressed[pygame.K_a]
                    other_player.did_press_jump = player_two_button.keys_pressed[pygame.K_w]
            else:
                self.did_press_right = player_one_button.keys_pressed[pygame.K_RIGHT]
                self.did_press_left = player_one_button.keys_pressed[pygame.K_LEFT]
                self.did_press_jump = player_one_button.keys_pressed[pygame.K_UP]
                other_player.did_press_right = player_one_button.keys_pressed[pygame.K_d]
                other_player.did_press_left = player_one_button.keys_pressed[pygame.K_a]
                other_player.did_press_jump = player_one_button.keys_pressed[pygame.K_w]

            if self.is_on_the_floor:
                if self.did_press_right:
                    self.vx = Constants.HORIZONTAL_WALKING_SPEED
                    self.player_legs.walk()
                elif self.did_press_left:
                    self.vx = -Constants.HORIZONTAL_WALKING_SPEED
                    self.player_legs.walk()
                else:
                    self.vx = 0
            else:
                if self.did_press_right:
                    self.vx = Constants.HORIZONTAL_AIR_SPEED
                elif self.did_press_left:
                    self.vx = -Constants.HORIZONTAL_AIR_SPEED
            if self.did_press_jump and self.is_on_the_floor:
                self.vy = Constants.JUMP_VY
                self.is_on_the_floor = False
            if other_player.is_on_the_floor:
                if other_player.did_press_right:
                    other_player.vx = Constants.HORIZONTAL_WALKING_SPEED
                    other_player.player_legs.walk()
                elif other_player.did_press_left:
                    other_player.vx = -Constants.HORIZONTAL_WALKING_SPEED
                    other_player.player_legs.walk()
                else:
                    other_player.vx = 0
            else:
                if other_player.did_press_right:
                    other_player.vx = Constants.HORIZONTAL_AIR_SPEED
                elif other_player.did_press_left:
                    other_player.vx = -Constants.HORIZONTAL_AIR_SPEED
            if other_player.did_press_jump and other_player.is_on_the_floor:
                other_player.vy = Constants.JUMP_VY
                other_player.is_on_the_floor = False

            if not self.is_aiming and player_one_button.mouse_right_button:
                self.is_aiming = True
                self.reloading_timer.start()
            # if self.is_aiming and not player_one_button.mouse_right_button and self.reloading_timer.is_ready_to_shot():
            #     list_of_spirit.add(Arrow.Arrow(self, player_one_button.mouse_x_pos, player_one_button.mouse_y_pos))
            #     self.is_aiming = False

            if self.is_aiming and not player_one_button.mouse_right_button:
                if self.reloading_timer.is_ready_to_shot():
                    list_of_spirit.add(Arrow.Arrow(self, player_one_button.mouse_x_pos, player_one_button.mouse_y_pos))
                self.is_aiming = False

            if self.is_aiming:
                self.player_body.aim(player_one_button.mouse_x_pos, self.player_legs.rect.midtop[0])
            else:
                self.player_body.reverse_aim(player_one_button.mouse_x_pos, self.player_legs.rect.midtop[0])
            self.player_head.look(player_one_button.mouse_x_pos, self.player_legs.rect.midtop[0])
            if self.is_online:
                if not other_player.is_aiming and player_two_button.mouse_right_button:
                    other_player.is_aiming = True
                    other_player.reloading_timer.start()

                # if other_player.is_aiming and not player_two_button.mouse_right_button:
                #     # shot
                #     other_player.reloading_timer.start()
                #     list_of_spirit.add(Arrow.Arrow(other_player, player_two_button.mouse_x_pos, player_two_button.mouse_y_pos))
                #     other_player.is_aiming = False

                if other_player.is_aiming and not player_two_button.mouse_right_button:
                    if other_player.reloading_timer.is_ready_to_shot():
                        list_of_spirit.add(
                            Arrow.Arrow(other_player, player_two_button.mouse_x_pos, player_two_button.mouse_y_pos))
                    other_player.is_aiming = False

                if other_player.is_aiming:
                    other_player.player_body.aim(player_two_button.mouse_x_pos, other_player.player_legs.rect.midtop[0])
                else:
                    other_player.player_body.reverse_aim(player_two_button.mouse_x_pos,
                                                         other_player.player_legs.rect.midtop[0])
                other_player.player_head.look(player_two_button.mouse_x_pos, other_player.player_legs.rect.midtop[0])

        for spirit in [self.player_legs, self.player_body, self.player_head]:
            list_of_collided = pygame.sprite.spritecollide(spirit, list_of_spirit, False)
            for spirit_that_collided in list_of_collided:
                if spirit.type == spirit_that_collided.type:
                    continue
                if spirit_that_collided.type in other_player.player_spirits_types and self.player_num == 1:
                    self.collision_direction, self.collision_diff = get_collision_direction(spirit.my_rect,
                                                                                            spirit_that_collided.my_rect)
                    if self.collision_direction in [Direction.RIGHT, Direction.LEFT]:
                        if (self.vx > 0 and other_player.vx < 0) or (self.vx < 0 and other_player.vx > 0):
                            self.collision_diff = int(self.collision_diff / 2) + 1
                            if self.collision_direction == Direction.RIGHT:
                                self.vx = 0
                                self.x -= self.collision_diff
                                other_player.x += self.collision_diff
                                other_player.vx = 0
                            elif self.collision_direction == Direction.LEFT:
                                self.vx = 0
                                self.x += self.collision_diff + 1
                                other_player.x -= self.collision_diff + 1
                                other_player.vx = 0
                        elif self.vx == 0 and other_player.vx != 0:
                            if self.collision_direction == Direction.RIGHT:
                                other_player.vx = 0
                                other_player.x += self.collision_diff + 1
                            elif self.collision_direction == Direction.LEFT:
                                other_player.vx = 0
                                other_player.x -= self.collision_diff + 1
                        elif other_player.vx == 0 and self.vx != 0:
                            if self.collision_direction == Direction.RIGHT:
                                self.vx = 0
                                self.x -= self.collision_diff + 1
                            elif self.collision_direction == Direction.LEFT:
                                self.vx = 0
                                self.x += self.collision_diff + 1
                        elif self.vx == 0 and other_player.vx == 0:
                            pass
                    else:
                        if self.collision_direction == Direction.DOWN and self.vy > 0:  # may sitch
                            self.vy = 0
                            self.y -= self.collision_diff
                            self.is_on_the_floor = True
                        elif self.collision_direction == Direction.UP and other_player.vy > 0:  # may sitch
                            other_player.vy = 0
                            other_player.y -= self.collision_diff
                            other_player.is_on_the_floor = True

                elif spirit_that_collided.type == SpiritType.BLOCK:
                    self.collision_direction, self.collision_diff = get_collision_direction(spirit.my_rect,
                                                                                            spirit_that_collided.my_rect)
                    if self.collision_direction == Direction.RIGHT and self.vx > 0:
                        self.vx = 0
                        self.x -= self.collision_diff
                    elif self.collision_direction == Direction.LEFT and self.vx < 0:
                        self.vx = 0
                        self.x += self.collision_diff
                    elif self.collision_direction == Direction.DOWN and self.vy > 0 and spirit.type in [
                        SpiritType.PLAYER_1_LEGS, SpiritType.PLAYER_2_LEGS]:
                        self.vy = 0
                        self.y -= self.collision_diff
                        self.is_on_the_floor = True
                    elif self.collision_direction == Direction.UP and self.vy < 0:
                        self.vy = 0
                        self.y += self.collision_diff
                elif spirit_that_collided.type == SpiritType.ARROW:
                    if spirit.type in [SpiritType.PLAYER_2_HEAD, SpiritType.PLAYER_1_HEAD]:
                        self.health -= spirit_that_collided.get_damage()
                    self.health -= spirit_that_collided.get_damage()
                    spirit_that_collided.kill()
                    list_of_spirit.remove(spirit_that_collided)

                self.update_spirits()
                other_player.update_spirits()
        self.did_press_right, self.did_press_left, self.did_press_jump = None, None, None
        other_player.did_press_right, other_player.did_press_left, other_player.did_press_jump = None, None, None

    def is_dead(self) -> bool:
        return self.health < 0
