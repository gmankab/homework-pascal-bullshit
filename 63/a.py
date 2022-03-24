from dataclasses import dataclass
import pathlib
import sys
import os


for i in (
    str(pathlib.Path(__file__).parent),
    f'{pathlib.Path(__file__).parent}/libs.zip',
    f'{pathlib.Path(__file__).parent}/pygame',
):
    if i not in sys.path:
        sys.path.append(i)

from keyboard import is_pressed as is_pr
import pygame as pg
from functions import *
from data import *


def main():
    while True:
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
        text('exit?')
        text(
            f'fps - {round(clock.get_fps())}',
            dest = [-1, 0],
            from_end = True,
        )
        pg.display.update()
        win.win.fill(Color.background)


def move_window(start_x, start_y, new_x, new_y):
    window_x, window_y = os.environ['SDL_VIDEO_WINDOW_POS'].split(',')
    dist_x = new_x - start_x
    dist_y = new_y - start_y
    os.environ[
        'SDL_VIDEO_WINDOW_POS'
    ] = f'{win.width + dist_x}, {window_y + dist_y}'

    # Windows bugfix
    win.width += 1 if win.width % 2 == 0 else -1 
    win.win = pg.display.set_mode(win.size, pg.NOFRAME)

# main()

import time
time.sleep(2)
