# -*- coding: utf-8 -*-

import numpy as np
import crule
import copy
import constants

class Board(object):
    ROW = 10
    COL = 9

    def __init__(self, mode=0):
        if mode == 1:
            self.__board = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 5, 0, 0, 0, 0, 0, 5, 0],
                                     [6, 0, 6, 0, 6, 0, 6, 0, 6],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [16, 0, 16, 0, 16, 0, 16, 0, 16],
                                     [0, 15, 0, 0, 0, 0, 0, 15, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [11, 12, 13, 14, 17, 14, 13, 12, 11]])
        elif mode == 0:
            self.__board = np.array([[11, 12, 13, 14, 17, 14, 13, 12, 11],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 15, 0, 0, 0, 0, 0, 15, 0],
                                     [16, 0, 16, 0, 16, 0, 16, 0, 16],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [6, 0, 6, 0, 6, 0, 6, 0, 6],
                                     [0, 5, 0, 0, 0, 0, 0, 5, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [1, 2, 3, 4, 7, 4, 3, 2, 1]])

        self.__baseRule = crule.Rule()
        self.__rules = [crule.CannonRule(), crule.ElephantRule(), crule.KingRule(), crule.KnightRule(), crule.MandarinRule(), crule.PawnRule(), crule.RookRule()]
        self.__turn = crule.TurnRule()

    def update(self, board, turn):
        self.__board = copy.copy(board)
        self.__turn = copy.copy(turn)

    def get(self, row, col):
        return self.__board[row, col]

    def getPieces(self):
        result = []
        for row in range(Board.ROW):
            for col in range(Board.COL):
                if self.__board[row][col] != 0:
                    result.append((self.__board[row][col], (row, col)))
        return result

    def move(self, c, src, dst):
        isValid, isFihished = self.checkMovement(c, src, dst)
        if isValid:
            row_src, col_src = src
            row_dst, col_dst = dst
            self.__board[row_dst, col_dst] = self.__board[row_src, col_src]
            self.__board[row_src, col_src] = 0
            self.__turn.nextTurn()
        return isValid, isFihished

    def checkMovement(self, c, src, dst):
        if not self.__turn.check(src,  self.__board):
            return False, False
        baseRule = self.__baseRule.check(src, dst, self.__board)
        if not baseRule[0]:
            return False, False

        for v in self.__rules:
            isValid, isFihished = v.check(src, dst, self.__board)
            if isValid:
                return True, isFihished
        return False, False

    def isSameSide(self, src, dst):
        return self.__baseRule.isSameSide(src, dst, self.__board)

    def clone(self):
        b = Board()
        b.update(self.__board, self.__turn)
        return b

    def getTurn(self):
        return self.__turn

    def getBoard(self):
        return self.__board

    def isTurnRight(self, src):
        row, col = src
        if self.__turn.currentTurn() == constants.RED_TURN:
            return self.__board[row, col] < constants.BLACK_RED_LINE and self.__board[row, col] != 0
        else:
            return self.__board[row, col] > constants.BLACK_RED_LINE

if __name__ == '__main__':
    print 'hello world'


