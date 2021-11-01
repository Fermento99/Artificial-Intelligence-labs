# Paweł Kajanek


from math import sqrt
from board import Board


def wellPlaced(state: list[int], objective: list[int]) -> int:
    count = 0
    for i in range(Board.size**2):
        if i != 15 and state[i] != objective[i]:
            count += 1

    return count


def manhattan(state: list[int], objective: list[int]) -> int:
    count = []
    for i in range(Board.size**2):
        si = state.index(i)
        oi = objective.index(i)
        ix, iy = si % Board.size, si // Board.size
        jx, jy = oi % Board.size, oi // Board.size
        count.append(abs(ix - jx) + abs(iy - jy))
    return sum(count)

def noHeuristic(state: list[int], objective: list[int],):
    return 0