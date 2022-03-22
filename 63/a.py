import pathlib
import sys
from typing import Iterable
from pprint import pp

sys.path.append(str(pathlib.Path(__file__).parent))
sys.path.append(f'{pathlib.Path(__file__).parent}/libs.zip')
sys.path.append(f'{pathlib.Path(__file__).parent}/pygame')

from functions import *
from data import *
import pygame as pg
from keyboard import is_pressed as is_pr
from dataclasses import dataclass
import os


pg.init()
pg.display.set_caption('gmanka')


win = pg.display.set_mode(Scr.size)
clock = pg.time.Clock()


def exit():
    pg.quit()
    sys.exit()


def mode(val: str = None) -> None | str:
    if val:
        if Scr.mode != val:
            Scr.mode = val
            print(f'mode = {val}')
            return None
    else:
        return Scr.mode


def text(  # TODO cache
    text: str,
    dest: list = (0, 0),
    font_size: int = 50,
    font: str = 'Jet Brains Mono',
    color: tuple | list = Color.white,
    antialias: bool = True,
    from_end: bool = False,
):
    for index, item in enumerate(dest):
        if item < 0:
            dest[index] = Scr.size[index] - font_size * len(font)
    win.blit(
        pg.font.SysFont(
            font,
            font_size
        ).render(
            text,
            antialias,
            color,
        ),
        dest,
    )

pp(os.environ)

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
    text('exit?')
    text(
        f'fps - {round(clock.get_fps())}',
        dest = [-1, 0],
        from_end = True,
    )
    pg.display.update()
    win.fill((20, 20, 20))


def move_window(start_x, start_y, new_x, new_y):
    window_x, window_y = eval(os.environ['SDL_VIDEO_WINDOW_POS'])
    dist_x, dist_y = new_x - start_x, new_y - start_y
    os.environ[
        'SDL_VIDEO_WINDOW_POS'
    ] = f'{Scr.width + dist_x}, {window_y + dist_y}'

    # Windows HACK
    window_size_x += 1 if window_size_x % 2 == 0 else -1 

    screen = pygame.display.set_mode((window_size_x, window_size_y), pygame.NOFRAME)

