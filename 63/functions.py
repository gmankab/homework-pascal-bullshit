from data import *
import pygame as pg
import sys
import os


def aa_rect(surface, rect, color, radius=1):
    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """
    rect         = pg.Rect(rect)
    color        = pg.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0, 0
    rectangle    = pg.Surface(rect.size, pg.SRCALPHA)

    circle = pg.Surface(
        [min(rect.size) * 3] * 2, pg.SRCALPHA
    )
    pg.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pg.transform.smoothscale(
        circle, [int(min(rect.size) * radius)] * 2
    )

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags = pg.BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags = pg.BLEND_RGBA_MIN)

    return surface.blit(rectangle, pos)


def exit():
    pg.quit()
    sys.exit()


def mode(val: str = None) -> None | str:
    if val:
        if win.mode != val:
            win.mode = val
            print(f'mode = {val}')
            return None
    else:
        return win.mode


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
            dest[index] = win.size[index] - font_size * len(font)
    win.win.blit(
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
