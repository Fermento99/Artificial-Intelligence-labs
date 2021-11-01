# Paweł Kajanek

import sys

from board import Board, moveRandomly
from heuristic import wellPlaced, manhattan, noHeuristic
from utils import shuffle


def printResult(visited: dict, currState: Board, display=0):
    parent = visited[currState.frags]
    if display == 2:
        print(currState)
    elif display == 1:
        print(currState.howToMove(parent), end=' ')

    path = 0
    while parent != (0, 0):
        currState = Board(parent)
        parent = visited[currState.frags]
        if display == 2:
            print(currState)
        elif display == 1:
            print(currState.howToMove(parent), end=' ')
        path += 1
    print('\n\tvisited states: {}\n\tlength of found path: {}'.format(len(visited), path))


def astar(objective: list[int], heuristic: callable):
    end = Board(objective)
    start = Board(tuple([i for i in range(Board.size**2)]))
    open = {start.frags: (start, (0, 0))}
    closed = {}

    # print(end)

    while len(open) > 0:
        # if len(closed) % 1_000 == 0:
        #     print('closed: {:.3f}; open: {:.3f}'.format(len(closed)/1_000_000, len(open)/1_000_000), end='\r')

        currState, parent = min(open.values(), key=lambda entr: entr[0].getCombinedDist())

        open.pop(currState.frags)
        closed[currState.frags] = parent

        if currState.frags == end.frags:
            print('\t\t\t\t', end='\r')
            printResult(closed, currState, 1)
            break

        # print('{}'.format(currState.heurDist), end='\r')

        for move in currState.getMoves():
            state = currState.fragsAfterMove(move)
            child = Board(state)

            if child.frags in closed.keys():
                continue

            child.jumpDist = currState.jumpDist + 1
            child.heurDist = heuristic(child.frags, end.frags)

            if child.frags in open.keys():
                if open[child.frags][0].getCombinedDist() > child.getCombinedDist():
                    open[child.frags] = (child, currState.frags)
                continue
            
            open[child.frags] = (child, currState.frags)


def test(boardCount: int, size: int, randomMoves=0, shuffleMoves=0, manHeu=False, wellHeu=False, noHeu=False ):
    Board.size = size
    perms = [[i for i in range(Board.size**2)] for _ in range(boardCount)]

    for perm in perms:
        if randomMoves > 0:
            perm = moveRandomly(randomMoves)
        elif shuffleMoves > 0:
            shuffle(perm, Board.size, shuffleMoves)

        print(Board(perm))
    
        if manHeu:
            print('manhattan:')
            astar(tuple(perm), manhattan)
            print()
        if wellHeu:
            print('well placed:')
            astar(tuple(perm), wellPlaced)
            print()
        if noHeu:
            print('no heuristic:')
            astar(tuple(perm), noHeuristic)
            print()
        print()
        print()


def main():
    test(10, 3, randomMoves=30, manHeu=True, wellHeu=True)

if __name__ == "__main__":
    main()
