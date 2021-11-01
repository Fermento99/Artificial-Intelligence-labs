# Paweł Kajanek

from math import floor
from random import random


def randomChoice(list: list):
    return list[floor(random() * len(list))]


def _rand(size) -> int:
    return floor(random() * (size ** 2 - 1))


def getRand(size: int) -> tuple[int, int]:
    x = _rand(size)
    y = _rand(size)
    while x == y:
        y = _rand(size)

    return x, y


def shuffle(tbl: list, size: int, times=10) -> None:
    for _ in range(times):
        x, y = getRand(size)
        swap(tbl, x, y)
        x, y = getRand(size)
        swap(tbl, x, y)


def swap(tbl: list, pos1: int, pos2: int) -> None:
    tbl[pos1], tbl[pos2] = tbl[pos2], tbl[pos1]
    return tbl
