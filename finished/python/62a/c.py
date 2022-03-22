import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent)
)

from animals import *


pets = [
    Cat('Мурзик', 3),
    Turtle('Зак', 32),
    Dog('Шарик', 5),
    Snake('Чаки', 2),
]

for p in pets:
    p.say()
    if isinstance(p, Mammal):
        p.run()
    elif isinstance(p, Reptile):
        p.crawl()    
