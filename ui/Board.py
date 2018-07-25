# -*- coding: utf-8 -*-

import numpy as np
import crule

class Board(object):
    __ROW = 10
    __COL = 9

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

        self.__rules = [crule.CannonRule(), crule.ElephantRule(), crule.KingRule(), crule.KnightRule(), crule.MandarinRule(), crule.PawnRule(), crule.RookRule()]

    def update(self, board):
        self.__board = board

    def get(self, row, col):
        return self.__board[row, col]

    def putPieces(self, env):
        for row in range(Board.__ROW):
            for col in range(Board.__COL):
                if self.__board[row][col] != 0:
                    env.putPiece(self.__board[row][col], (row, col))

    def move(self, c, src, dst):
        isValid = False
        isFihished = False
        for v in self.__rules:
            isValid, isFihished = v.check(src, dst, self.__board)
            if isValid:
                row_src, col_src = src
                row_dst, col_dst = dst
                self.__board[row_dst, col_dst] = self.__board[row_src, col_src]
                self.__board[row_src, col_src] = 0
                break
        return isValid, isFihished

if __name__ == '__main__':
    print("hello world")
