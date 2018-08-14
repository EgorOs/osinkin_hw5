#!/usr/bin/env python3
from functools import reduce


def is_armstrong(number):
    if not isinstance(number, int):
        raise TypeError('{} is {}, not int'.format(number, type(number).__name__))
    if number < 1:
        raise ValueError(str(number) + " is not natural a number")
    n = str(number)
    lst = [int(x)**len(n) for x in n]
    if number == reduce(lambda x, y: x+y, lst):
        return True
    else:
        return False


assert is_armstrong(153) == True, "Armstrong's number"
assert is_armstrong(10) == False, "Not armstrong's number"
