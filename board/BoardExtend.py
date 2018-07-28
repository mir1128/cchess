# -*- coding: utf-8 -*-

from Board import Board
import constants


class BoardExtend(Board):
    def __init__(self):
        super(Board, self).__init__()

    def nexPossibleMovements(self):

        possible_movements = []

        pieces = self.getThisTurnPieces()

        for p in pieces:
            self.get(p)



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


if __name__ == '__main__':
    print "hello world"
