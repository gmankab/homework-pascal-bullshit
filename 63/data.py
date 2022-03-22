from dataclasses import dataclass


@dataclass()
class Scr:
    width = 1000
    height = 600
    size = [width, height]
    mode = 'main'


@dataclass()
class Color:
    black =      (0,   0,   0)
    white =      (255, 255, 255)
    background = (20, 20, 20)
