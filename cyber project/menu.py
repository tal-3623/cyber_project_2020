import pygame

from client import draw_image
from input import Buttons

main_screen = 'stick_AME\\main_screen.png'
info_screen = 'stick_AME\\info_screen.png'
setting_screen_wasd = 'stick_AME\\wasd.png'
setting_screen_arrows = 'stick_AME\\arrows_setting.png'


play_button = (817, 1136, 91, 206)  # L,R,U,D
info_button = (817, 1136, 297, 412)
setting_button = (600, 1144, 482, 576)
exit_button = (343, 561, 600, 680)

back_button = (926, 1170, 600, 680)

arrows_button = (787, 1150, 40, 275)
wasd_button = (787, 1150, 315, 545)


def is_mouse_in_area(button: Buttons, area) -> bool:
    left = area[0]
    right = area[1]
    up = area[2]
    down = area[3]
    x = button.mouse_x_pos
    y = button.mouse_y_pos
    return left < x < right and up < y < down


class Menu:

    def __init__(self):
        self.is_mouse_pressed = False
        self.is_arrows = True

    def run(self, button: Buttons, screen):
        draw_image(screen, main_screen, 0, 0)
        screen_name = main_screen
        while True:
            button.update()
            if screen_name == main_screen:
                if is_mouse_in_area(button, play_button) and self.did_click(button):
                    break
                elif is_mouse_in_area(button, info_button) and self.did_click(button):
                    draw_image(screen, info_screen, 0, 0)
                    screen_name = info_screen
                elif is_mouse_in_area(button, setting_button) and self.did_click(button):
                    draw_image(screen, setting_screen_arrows, 0, 0)
                    screen_name = setting_screen_arrows
                    self.is_arrows = True
                elif is_mouse_in_area(button, exit_button) and self.did_click(button):
                    return True, self.is_arrows
            # -----------------------------------------
            elif screen_name == info_screen:
                if is_mouse_in_area(button, back_button) and self.did_click(button):
                    draw_image(screen, main_screen, 0, 0)
                    screen_name = main_screen
            # ------------------------------------------------
            elif screen_name == setting_screen_wasd or screen_name == setting_screen_arrows:
                if is_mouse_in_area(button, wasd_button) and self.did_click(button):
                    draw_image(screen, setting_screen_wasd, 0, 0)
                    screen_name = setting_screen_wasd
                    self.is_arrows = False
                elif is_mouse_in_area(button, arrows_button) and self.did_click(button):
                    draw_image(screen, setting_screen_arrows, 0, 0)
                    screen_name = setting_screen_arrows
                    self.is_arrows = True
                elif is_mouse_in_area(button, back_button) and self.did_click(button):
                    draw_image(screen, main_screen, 0, 0)
                    screen_name = main_screen
            # ------------------------------------
            pygame.display.flip()

        return False, self.is_arrows

    def did_click(self, button: Buttons):
        if not self.is_mouse_pressed and button.mouse_left_button:
            self.is_mouse_pressed = True
        elif self.is_mouse_pressed and not button.mouse_left_button:
            self.is_mouse_pressed = False
            return True
        return False
