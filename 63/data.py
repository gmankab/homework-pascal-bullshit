from dataclasses import dataclass
import pygame as pg
import os


class Win:
    size = [1000, 600]

    @property
    def width(self):
        return self.size[0]

    @width.setter
    def width(self, val):
        self.size[0] = val

    mode = 'main'
    win = pg.display.set_mode(size)
    handle = pg.display.get_wm_info()['window']


@dataclass()
class Color:
    black =      (0,   0,   0)
    white =      (255, 255, 255)
    background = (20, 20, 20)


pg.init()
pg.display.set_caption('gmanka')
clock = pg.time.Clock()
win = Win()

from ctypes import windll


move = windll.user32.MoveWindow


print(pg.display.get_surface())


move(win.handle, 100, 0)
