# -*- coding: utf-8 -*-

import constants
from Rule import Rule
import numpy as np

class PawnRule(Rule):

    def __init__(self):
        super(PawnRule, self).__init__()

    def check(self, src, dst, board):
        row_src, col_src = src
        row_dst, col_dst = dst

        if (board[row_src, col_src] != constants.BLACK_PAWN) and (board[row_src, col_src] != constants.RED_PAWN):
            return False, False

        is_promoted, side = self.isPromoted(src, board)
        if constants.CHU == side:
            if is_promoted:
                return (row_src == row_dst and abs(col_src-col_dst) == 1) or (col_src == col_dst and row_dst - row_src == 1), super(PawnRule, self).isOverAfterStep(dst, board)
            else:
                return col_src == col_dst and row_dst - row_src == 1, super(PawnRule, self).isOverAfterStep(dst, board)
        elif constants.HAN == side:
            if is_promoted:
                return (row_src == row_dst and abs(col_src-col_dst) == 1) or (col_src == col_dst and row_src - row_dst == 1), super(PawnRule, self).isOverAfterStep(dst, board)
            else:
                return col_src == col_dst and row_src - row_dst == 1, super(PawnRule, self).isOverAfterStep(dst, board)

    def isPromoted(self, src, board):
        row_src, col_src = src
        if board[row_src, col_src] < constants.BLACK_RED_LINE:  # 红兵
            array_row, arr_col = np.where(board == constants.RED_KING)  # 找到红帅的位置
            if array_row[0] <= 4:
                return row_src > 4, constants.CHU
            else:
                return row_src <= 4, constants.HAN
        elif board[row_src, col_src] > constants.BLACK_RED_LINE:  # 黑卒
            array_row, arr_col = np.where(board == constants.BLACK_KING)  # 找到黑将的位置
            if array_row[0] <= 4:
                return row_src > 4, constants.CHU
            else:
                return row_src <= 4, constants.HAN


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

    p = PawnRule()
    try:
        print(p.check((3, 0), (4, 0), s1))
    except NameError, e:
        print(e.message)

    s2 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [0, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [6, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(p.check((5, 0), (6, 0), s2))
    except NameError, e:
        print(e.message)

    try:
        print(p.check((5, 0), (5, 1), s2))
    except NameError, e:
        print(e.message)

    try:
        print(p.check((5, 0), (4, 0), s2))
    except NameError, e:
        print(e.message)

    s3 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [16, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(p.check((6, 0), (5, 0), s3))
    except NameError, e:
        print(e.message)

    s4 = np.array([[1, 2, 3, 4, 7, 4, 3, 2, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 5, 0, 0, 0, 0, 0, 5, 0],
                   [6, 0, 6, 0, 6, 0, 6, 0, 6],
                   [16, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 16, 0, 16, 0, 16, 0, 16],
                   [0, 15, 0, 0, 0, 0, 0, 15, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [11, 12, 13, 14, 17, 14, 13, 12, 11]])

    try:
        print(p.check((4, 0), (3, 0), s4))
    except NameError, e:
        print(e.message)


    try:
        print(p.check((4, 0), (4, 1), s4))
    except NameError, e:
        print(e.message)

    try:
        print(p.check((4, 0), (5, 0), s4))
    except NameError, e:
        print(e.message)















