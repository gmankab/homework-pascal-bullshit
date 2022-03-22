import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent)
)

from animals import *


pets = [
    Cat('Мурзик', 3),
    Dog('Шарик', 5),
]

for p in pets:
    p.say()
    p.run()
