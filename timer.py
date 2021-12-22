from inspect import cleandoc
from decimal import Decimal
import timeit

def b(num): # beautiful view of float num
    return str(Decimal(num))[:10]