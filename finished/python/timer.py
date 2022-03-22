import os
from decimal import Decimal
import timeit

def b(num): # beautiful view of float num
    return str(Decimal(num))[:10]


def get_time(func, arg):
    start_time = timeit.default_timer()
    func(arg)
    end_time = timeit.default_timer()
    return b(end_time - start_time)


print(
    get_time(
        os.system,
        'prime_numbers_sieve_of_Eratosthenes.exe'
    ),
    get_time(
        os.system,
        'prime_numbers_brute_force.exe'
    )
)
