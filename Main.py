import time
from os import environ
from sys import exit

from Tank import Tank

environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "True")
from pygame import display, draw, event
from pygame.constants import *
from pygame.colordict import *

if __name__ == '__main__':

    display.init()
    surf = display.set_mode((640, 480))
    display.set_caption("pyGame")

    p1 = Tank()

    move_str = ""
    shooting_dire = ""
    move = False
    move_r = 0
    while True:
        # surf.blit(surf, (0, 0))
        for e in event.get():
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN:
                if e.key == K_j:
                    p1.shooting(shooting_dire)
                if e.key == K_w or e.key == K_UP:
                    if "up" in move_str:
                        move_str = move_str.replace(",up", "")
                    move_str += ",up"
                if e.key == K_s or e.key == K_DOWN:
                    if "down" in move_str:
                        move_str = move_str.replace(",down", "")
                    move_str += ",down"
                if e.key == K_a or e.key == K_LEFT:
                    if "left" in move_str:
                        move_str = move_str.replace(",left", "")
                    move_str += ",left"
                if e.key == K_d or e.key == K_RIGHT:
                    if "right" in move_str:
                        move_str = move_str.replace(",right", "")
                    move_str += ",right"
            if e.type == KEYUP:
                if e.key == K_w or e.key == K_UP:
                    if "up" in move_str:
                        move_str = move_str.replace(",up", "")
                if e.key == K_s or e.key == K_DOWN:
                    if "down" in move_str:
                        move_str = move_str.replace(",down", "")
                if e.key == K_a or e.key == K_LEFT:
                    if "left" in move_str:
                        move_str = move_str.replace(",left", "")
                if e.key == K_d or e.key == K_RIGHT:
                    if "right" in move_str:
                        move_str = move_str.replace(",right", "")
            # print(move_str)
        if move_str is not "" and time.time() - move_r > 0.02:
            move_r = time.time()
            move_str_s = move_str.split(",")[-1]
            shooting_dire = move_str_s
            if move_str_s == "up":
                p1.move(0, -1)
            if move_str_s == "down":
                p1.move(0, 1)
            if move_str_s == "left":
                p1.move(-1, 0)
            if move_str_s == "right":
                p1.move(1, 0)

        if p1.get_bullet_num() > 0:
            p1.bullet_move()

        surf.fill(THECOLORS["black"])
        draw.circle(surf, [255, 0, 255], p1.get_local(), 4, 3)
        if p1.get_bullet_num() > 0:
            for bullet in p1.get_bullet():
                draw.circle(surf, [255, 0, 255], bullet.get_local(), 4, 3)
        display.update()
        # display.flip()
