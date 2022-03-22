import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent))
sys.path.append(f'{pathlib.Path(__file__).parent}/libs.zip')

from functions import *
import pygame as pg
from keyboard import is_pressed as is_pr
from dataclasses import dataclass
import os


pg.init()
pg.display.set_caption('gmanka')


@dataclass()
class Scr:
    width = 1000
    height = 600
    size = [width, height]
    mode = 'main'


win = pg.display.set_mode((640, 480))
clock = pg.time.Clock()


def exit():
    pg.quit()
    sys.exit()


font = pg.font.SysFont('Open Sans', 25)


def mode(val: str = None):
    if val:
        if Scr.mode != val:
            Scr.mode = val
            print(f'mode = {val}')
            return None
    else:
        return Scr.mode


run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                exit()
            case pg.MOUSEBUTTONUP:
                pass

    if is_pr('esc'):
        exit()

    if is_pr('enter'):
        mode('exit')

    match mode():
        case 'exit':
            aa_rect(
                win,
                (0, 0, 100, 50),
                (100, 100, 100),
            )
            win.blit(font.render('exit?', True, (200, 200, 200), (0, 0, 0)))
    pg.display.update()
    win.fill((20, 20, 20))
    pg.display.flip()
