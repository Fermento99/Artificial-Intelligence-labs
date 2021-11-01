# Paweł Kajanek

from utils import swap, randomChoice


class Board:
    size = 4

    def __init__(self, frags: tuple[int]) -> None:
        self.frags = frags
        self.jumpDist = 0
        self.heurDist = 0

    def getCombinedDist(self) -> int:
        return self.heurDist + self.jumpDist

    def getMoves(self) -> list[int]:
        movable = self.frags.index(Board.size**2 - 1)
        x = movable % Board.size
        y = movable // Board.size
        UP = movable - Board.size
        DOWN = movable + Board.size
        LEFT = movable - 1
        RIGHT = movable + 1
        moves = [UP, DOWN, LEFT, RIGHT]

        if x == 0:
            moves.remove(LEFT)
        elif x == Board.size - 1:
            moves.remove(RIGHT)

        if y == 0:
            moves.remove(UP)
        elif y == Board.size - 1:
            moves.remove(DOWN)

        return moves

    def fragsAfterMove(self, postion: int) -> tuple[int]:
        copyFrags = list(self.frags)
        movable = self.frags.index(Board.size**2 - 1)
        swap(copyFrags, movable, postion)
        return tuple(copyFrags)

    def __str__(self) -> str:
        out = ""
        for i in range(0, Board.size):
            for j in range(0, Board.size):
                val = self.frags[i * Board.size + j]
                if val != Board.size**2 - 1:
                    out += "{:2d}  ".format(val)
                else:
                    out += "    "
            out += "\n"
        return out

    def __repr__(self) -> str:
        return str("Board: d={}, {}".format(self.getCombinedDist(), self.frags))

    def howToMove(self, parent: tuple):
        if parent != (0, 0):
            parentFrags = list(parent)
            diff = self.frags.index(self.size**2 - 1) - parentFrags.index(self.size**2 - 1)
            if diff == 1:
                return '←'
            elif diff == -1:
                return '→'
            elif diff > 0:
                return '↑'
            else:
                return '↓'
        return ''



def moveRandomly(moves: int):
    brd = Board(tuple([i for i in range(Board.size**2)]))
    for _ in range(moves):
        move = randomChoice(brd.getMoves())
        brd = Board(brd.fragsAfterMove(move))
    
    return brd.frags
