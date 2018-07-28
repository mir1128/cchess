# -*- coding: utf-8 -*-

from Board import Board
import constants


class BoardExtend(Board):
    def __init__(self):
        Board.__init__(self)

    def nextPossibleMovements(self):

        possible_movements = []

        for p in self.getThisTurnPieces():
            r, c = p
            for row in range(Board.ROW):
                for col in range(Board.COL):
                    is_valid, is_finished = self.checkMovement(self.get(r, c), p, (row, col))
                    if is_valid:
                        possible_movements.append((r, c, row, col))
        return possible_movements

    def getThisTurnPieces(self):
        pieces_can_move = []

        for r in range(Board.ROW):
            for c in range(Board.COL):
                if self.getBoard()[r, c] != 0:
                    if self.getTurn().currentTurn() == constants.RED_TURN:
                        if self.getBoard()[r, c] < constants.BLACK_RED_LINE:
                            pieces_can_move.append((r, c))
                    else:
                        if self.getBoard()[r, c] > constants.BLACK_RED_LINE:
                            pieces_can_move.append((r, c))
        return pieces_can_move

    def clone(self):
        b = BoardExtend()
        b.update(self.getBoard(), self.getTurn())
        return b

    def output(self):
        turn = None
        if self.getTurn() == constants.RED_TURN:
            turn = 'red'
        else:
            turn = 'black'

        return turn + ' : ' + str(self.getBoard().tolist())


if __name__ == '__main__':
    b = BoardExtend()

    print b.nextPossibleMovements()
