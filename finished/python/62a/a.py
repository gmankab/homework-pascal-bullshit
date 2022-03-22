import sys
import pathlib

sys.path.append(
    str(pathlib.Path(__file__).parent)
)

from animals import *


p = Dog('Шарик', 5)
p.make_older()
p.say(p.age)

pets = [
    Cat('Мурка', 3),
    p
]

for p in pets:
    p.say()
