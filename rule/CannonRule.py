# -*- coding: utf-8 -*-

import constants
from Rule import Rule
import numpy as np


class CannonRule(Rule):
    def __init__(self):
        super(CannonRule, self).__init__()

    def check(self, src, dst, board):
        super(CannonRule, self).check(src, dst, board)

        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_CANNON) and (board[row_src, col_src] != constants.RED_CANNON):
            return False, False

        # 起点和终点不在一条线上
        if (row_src != row_dst) and (col_src != col_dst):
            return False, False

        # 在同一行
        if row_src == row_dst:
            if all(v == 0 for v in board[row_src, min(col_src, col_dst) + 1: max(col_src, col_dst)].tolist()):
                return True, super(CannonRule, self).isOverAfterStep(dst, board)
            if board[row_dst, col_dst] != 0 and (not self.isSameSide(src, dst, board)):
                arr = np.where(board[row_src, min(col_src, col_dst) + 1: max(col_src, col_dst)] != 0)
                return arr[0].size == 1, super(CannonRule, self).isOverAfterStep(dst, board)
            return False, False
        elif col_src == col_dst:
            if all(v == 0 for v in board[min(row_src, row_dst) + 1:  max(row_src, row_dst), col_src].tolist()):
                return True, super(CannonRule, self).isOverAfterStep(dst, board)
            if board[row_dst, col_dst] != 0 and (not self.isSameSide(src, dst, board)):
                arr = np.where(board[min(row_src, row_dst) + 1: max(row_src, row_dst), col_src] != 0)
                return arr[0].size == 1, super(CannonRule, self).isOverAfterStep(dst, board)
            return False, False
        else:
            return False, False

    def isSameSide(self, src, dst, board):
        row_src, col_src = src
        row_dst, col_dst = dst

        if board[row_src, col_src] < constants.BLACK_RED_LINE and board[row_dst, col_dst] < constants.BLACK_RED_LINE:
            return True
        if board[row_src, col_src] > constants.BLACK_RED_LINE and board[row_dst, col_dst] > constants.BLACK_RED_LINE:
            return True
        return False


if __name__ == '__main__':
    s1 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])
    c = CannonRule()

    try:
        print(c.check((2, 1), (2, 6), s1))
    except NameError, e:
        print(e.message)

    try:
        print(c.check((2, 1), (9, 1), s1))
    except NameError, e:
        print(e.message)

    s2 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 5, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(c.check((6, 1), (6, 4), s2))
    except NameError, e:
        print(e.message)

    s3 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 5, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(c.check((4, 4), (9, 4), s3))
    except NameError, e:
        print(e.message)